from Tkinter import *
from urllib import urlopen, urlretrieve

import tkFileDialog
import os
from FileWriter import *
import commands
import re


def buildLibrary(parentFrame, directory, compileType, buildType, mxmlcPath):
    generateASFiles(directory, directory, buildType)
    buildLinkerASFile(directory, directory)
    flexBuild(directory, compileType, mxmlcPath)
    removeASFiles(directory)
    
    
def generateASFiles(directory, startPath, buildType):
    dirList = os.listdir(directory)
    
    #Check each item in the current directory.
    for item in dirList:
        currentPath = (directory + "/" + item)
        
        #Directory: Recurse.
        if os.path.isdir(currentPath):
            generateASFiles(currentPath, startPath, buildType)
            
        #File: Check if it's an image.
        else:
            fileName = item.rsplit('.')
            extension = fileName[len(fileName) - 1]
            
            #Chack the extension is a media type that can be embedded.
            if buildType == "BitmapData" and extension in bitmapTypes:
                if checkName(fileName[0]):
                    createASBitmapFile(directory, startPath, fileName)
                    
            elif buildType == "Sprite" and extension in spriteTypes:
                if checkName(fileName[0]):
                    createASSpriteFile(directory, startPath, fileName)
                
            elif buildType == "Audio" and extension in audioTypes:
                if checkName(fileName[0]):
                    createASAudioFile(directory, startPath, fileName)
                    
            elif buildType == "XML":
                if checkName(fileName[0]):
                    createASXMLFile(directory, startPath, fileName)
            
            
            elif buildType == "All" and extension in allTypes:
                #Check that the name wont crash mxmlc
                if checkName(fileName[0]):
                    #Build the appropriate type depending on the extension of the file.
                    if extension in spriteTypes:
                        createASSpriteFile(directory, startPath, fileName)
                    elif extension in audioTypes:
                        createASAudioFile(directory, startPath, fileName)
  
  
  
  
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
    
    

