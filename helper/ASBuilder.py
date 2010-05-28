from Tkinter import *
from urllib import urlopen, urlretrieve

import tkFileDialog
import os
from FileWriter import *

imageTypes = ["png", "jpg", "bmp"]

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
            
        #File: Check if it's an image.
        else:
            fileName = item.rsplit('.')
            
            if fileName[len(fileName) - 1] == "xml":
                #Image: Build the AS file.
                createASXMLFile(directory, startPath, fileName)

