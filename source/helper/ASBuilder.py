from Tkinter import *
from urllib import urlopen, urlretrieve

import tkFileDialog
import os
from FileWriter import *
import commands
import re

ttkAvail = True
try:
    import ttk
except:
    print "Warning: python version < 2.7, some features disabled.\n\t1 - Progress Bar."
    ttkAvail = False


bitmapTypes = ["png", "jpg", "gif", "jpeg"]
spriteTypes = ["png", "jpg", "gif", "jpeg", "svg"]

validName = re.compile("(?:(?:[_]|[a-z]|[A-Z])+[0-9]*)")



def buildLibrary(parentFrame, directory, compileType, buildType, mxmlcPath):
    progBar = None
    
    if ttkAvail:
        progBar = ttk.Progressbar(parentFrame, orient=HORIZONTAL, value=0, length=200, mode='determinate')
        progBar.pack()
        parentFrame.update()
        
    if buildType == "BitmapData":
        generateASBitmapFiles(directory, directory)
    elif buildType == "Sprite":
        generateASSpriteFiles(directory, directory)
    elif buildType == "XML":
        generateASXMLFiles(directory, directory)

    if progBar != None:
        progBar.step(15)
        parentFrame.update()
    
    buildLinkerASFile(directory, directory)
    if progBar != None:
        progBar.step(15)
        parentFrame.update()
    
    flexBuild(directory, compileType, mxmlcPath)
    if progBar != None:
        progBar.step(50)
        parentFrame.update()
    
    removeASFiles(directory)
    if progBar != None:
        progBar.step(19)
        parentFrame.update()
        progBar.pack_forget()
    
    
    
def checkName(name):
    tokens = re.findall(validName, name)
    if tokens[0] != name:
        showWarning("Naming Error!", ("Name does not meet naming requirements:\n%s" % name))
        return False
    
    return True



def flexBuild(directory, compileType, mxmlcPath):
    base = directory.split('/')[len(directory.split('/'))-1] + ".as"
    mxBase = directory + "/" + base

    if (compileType == "SWC"):
        command = "%scompc -source-path %s -include-sources %s/%s -output '%s/%s.swc'" % (mxmlcPath, directory, directory, base, directory, base.split('.')[0])
    elif (compileType == "SWF"):
        command = "%smxmlc %s -output '%s/%s.swf'" % (mxmlcPath, mxBase, directory, base.split('.')[0])
    else:
        showError("Compiler Error!", "Error in compile type.")
        
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
    for i in range(len(asFiles)):
        asFiles.pop()
    
    
    
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
            
            if fileName[len(fileName) - 1] in bitmapTypes:
                if checkName(fileName[0]):
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
            
            if fileName[len(fileName) - 1] in spriteTypes:
                if checkName(fileName[0]):
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
                if checkName(fileName[0]):
                
                    #Image: Build the AS file.
                    createASXMLFile(directory, startPath, fileName)

