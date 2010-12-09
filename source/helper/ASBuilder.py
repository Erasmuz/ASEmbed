from Tkinter import *
from urllib import urlopen, urlretrieve

import tkFileDialog
import os
from FileWriter import *
import commands

imageTypes = ["png", "jpg", "bmp"]


def buildLibrary(directory, compileType, buildType):
    if buildType == "Bitmaps":
        generateASBitmapFiles(directory, directory)
    elif buildType == "Sprites":
        generateASSpriteFiles(directory, directory)
    elif buildType == "XML":
        generateASXMLFiles(directory, directory)

        
    buildLinkerASFile(directory, directory)
    flexBuild(directory)
    
    removeASFiles(directory)


def flexBuild(directory):
    base = directory.split('/')[len(directory.split('/'))-1] + ".as"
    command = "compc -source-path %s -include-sources %s/%s -output '%s/%s.swc'" % (directory, directory, base, directory, base.split('.')[0])
    #command = "mxmlc -source-path %s -output '%s/%s.swf'" % (directory, directory, base.split('.')[0])
    
    returnCode, consoleOutput = commands.getstatusoutput(command)

    if str(returnCode) == "32512":
        showError("Compiler Error!", "MXMLC/COMPC not found.\nMake sure these are in your environment path.")
    else:
        os.system(command)
    
def removeASFiles(directory):
    #Remove the file from the hard drive.
    for item in asFiles:
        os.remove(item)
    
    #Remove the files from the stack
    for item in asFiles:
        asFiles.pop(0)
    
    
def generateASBitmapFiles(directory, startPath):
    dirList = os.listdir(directory)
    
    #Check each item in the current directory.
    for item in dirList:
        currentPath = (directory + "/" + item)
        
        #Directory: Recurse.
        if os.path.isdir(currentPath):
            generateASBitmapFiles(currentPath, startPath)
            
        #File: Check if it's an image.
        else:
            fileName = item.rsplit('.')
            
            if fileName[len(fileName) - 1] in imageTypes:
                #Image: Build the AS file.
                createASBitmapFile(directory, startPath, fileName)
            
            
def generateASSpriteFiles(directory, startPath):
    dirList = os.listdir(directory)
    
    #Check each item in the current directory.
    for item in dirList:
        currentPath = (directory + "/" + item)
        
        #Directory: Recurse.
        if os.path.isdir(currentPath):
            generateASSpriteFiles(currentPath, startPath)
            
        #File: Check if it's an image.
        else:
            fileName = item.rsplit('.')
            
            if fileName[len(fileName) - 1] in imageTypes:
                #Image: Build the AS file.
                createASSpriteFile(directory, startPath, fileName)
                


def generateASXMLFiles(directory, startPath):
    dirList = os.listdir(directory)
    
    #Check each item in the current directory.
    for item in dirList:
        currentPath = (directory + "/" + item)
        
        #Directory: Recurse.
        if os.path.isdir(currentPath):
            generateASXMLFiles(currentPath, startPath)
            
        #File: Check if it's an xml file.
        else:
            fileName = item.rsplit('.')
            
            if fileName[len(fileName) - 1] == "xml":
                #Image: Build the AS file.
                createASXMLFile(directory, startPath, fileName)

