from Tkinter import *
from urllib import urlopen, urlretrieve

import tkFileDialog
import os

imageTypes = ["png", "jpg", "bmp"]

def createASBitmapFile(directory, startPath, fileName):
    output = "package "
    
    output += getPackagePath(directory, startPath)
    
    output += " {\n\
import flash.display.BitmapData;\n\
\n\
[Embed(source=\"%s.%s\")]\n\
public class %s extends BitmapData {\n\
    public function %s(width:int, height:int, transparent:Boolean=true, fillColor:uint=0xFFFFFF) {\n\
        super(width, height, transparent, fillColor);\n\
    }\n\
}\n\
}" % (fileName[0], fileName[len(fileName)-1], fileName[0], fileName[0])

    outputAS = open(( directory + "/" + fileName[0] + ".as"), 'w')
    outputAS.write(output)
    
    
def getPackagePath(directory, startPath):
    output = ""
    
    packagePath = directory.replace(startPath, "")
    
    path = packagePath.split('/')
    if len(path) > 1:
        path.pop(0)
    
    for i in range(len(path)-1):
        output += (path[i] + ".")
    output += (path[len(path)-1])
    
    return output
    
def createASSpriteFile(directory, startPath, fileName):
    print ""
    
    
def createASXMLFile(directory, startPath, fileName):
    print ""
    
    
def buildLinkerASFile(directory, startDirectory):
    linkerFile = open((directory + "/" + directory.split('/')[len(directory.split('/'))-1] + ".as"), 'w')
    
    linkerFile.write("package {\n")
    
    addASFilesToLinkerFile(directory, startDirectory, linkerFile)
    
    linkerFile.write("import flash.display.Sprite;\n\npublic class %s extends Sprite {\n" % directory.split('/')[len(directory.split('/'))-1])
    
def addASFilesToLinkerFile(directory, startDirectory, linkerFile):
    dirList = os.listdir(directory)
    
    #Check each item in the current directory.
    for item in dirList:
        currentPath = (directory + "/" + item)
        
        #Directory: Recurse.
        if os.path.isdir(currentPath):
            addASFilesToLinkerFile(currentPath, startDirectory, linkerFile)
            
        #File: Check if it's an .as file.
        else:
            fileName = item.rsplit('.')
            
            #Check here to make sure the file isn't the linker file. (Don't link it to itself!)
            if fileName[len(fileName) - 1] == "as":
                #HERE COULD BE A PROBLEM IF A USER CREATES FILE WITH '.' IN THEM
                addToImport(directory, startDirectory, fileName[0], linkerFile)
                
                
def addToImport(directory, startDirectory, item, linkerFile):
    packagePath = getPackagePath(directory, startDirectory)
    packagePath += "%s" % item if (packagePath == "") else ".%s" % item
    linkerFile.write("import %s\n" % packagePath)


