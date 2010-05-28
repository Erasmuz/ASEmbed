from Tkinter import *
from urllib import urlopen, urlretrieve

import tkFileDialog
import os

imageTypes = ["png", "jpg", "bmp"]

def createASBitmapFile(directory, startPath, fileName):
    output = "package "
    
    packagePath = directory.replace(startPath, "")
    
    path = packagePath.split('/')
    path.pop(0)
    
    for i in range(len(path)-1):
        output += (path[i] + ".")
    output += (path[len(path)-1])
    
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
    #outputAS.write(output)
    
    
def createASSpriteFile(directory, startPath, fileName):
    print ""
    
    
def createASXMLFile(directory, startPath, fileName):
    print ""
    
    
def buildLinkerASFile(directory, startDirectory):
    linkerFile = directory + "/" + directory.split('/')[len(directory.split('/'))-1] + ".as"
    
    print linkerFile
    
    
    
