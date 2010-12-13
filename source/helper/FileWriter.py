from Tkinter import *
from urllib import urlopen, urlretrieve

import os
import re

bitmapTypes = ["png", "jpg", "gif", "jpeg"]
spriteTypes = ["png", "jpg", "gif", "jpeg", "svg"]
audioTypes = ["mp3"]
allTypes = ["png", "jpg", "gif", "jpeg", "svg", "mp3"]
xmlTypes = ["xml"]

validName = re.compile("(?:(?:[_]|[a-z]|[A-Z])+[0-9]*)")

asFiles = []


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

    fileName = (directory + "/" + fileName[0] + ".as")
    
    asFiles.append(fileName)
    outputAS = open(fileName, 'w')
    outputAS.write(output)
    
    
def createASAudioFile(directory, startPath, fileName):
    output = "package "
    output += getPackagePath(directory, startPath)
    
    output += " {\n\
	import flash.media.Sound;\n\
\n\
[Embed(source=\"%s.%s\")]\n\
	final public class %s extends Sound\n\
	{\n\
\n\
\n\
		public function %s():void\n\
		{\n\
			super();\n\
		}\n\
\n\
	}\n\
}" % (fileName[0], fileName[len(fileName)-1], fileName[0], fileName[0])
    
    fileName = ( directory + "/" + fileName[0] + ".as")
    asFiles.append(fileName)
    
    try:
        outputAS = open(fileName, 'w')
    except:
        showError("Open Error!", "Error creating .as file to embed object:\n%s" % fileName)
        exit()
        
    try:
        outputAS.write(output)
    except:
        showError("Write Error!", "Could not write to created .as file.")
        exit()
    
    
def createASSpriteFile(directory, startPath, fileName):
    output = "package "
    output += getPackagePath(directory, startPath)
    
    output += " {\n\
import flash.display.DisplayObject;\n\
	import flash.display.MovieClip;\n\
\n\
	final public class %s extends MovieClip\n\
	{\n\
\n\
		[Embed(source=\"%s.%s\")]\n\
		private const Graphic:Class;\n\
\n\
		public function %s():void\n\
		{\n\
			super();\n\
			addCenteredChild(new Graphic());\n\
		}\n\
\n\
		private function addCenteredChild(child:DisplayObject):void\n\
		{\n\
			var c:DisplayObject = addChild(child);\n\
			c.x -= c.width;\n\
			c.y -= c.height;\n\
		}\n\
	}\n\
}" % (fileName[0], fileName[0], fileName[len(fileName)-1], fileName[0])
    
    fileName = ( directory + "/" + fileName[0] + ".as")
    asFiles.append(fileName)
    
    try:
        outputAS = open(fileName, 'w')
    except:
        showError("Open Error!", "Error creating .as file to embed object:\n%s" % fileName)
        exit()
        
    try:
        outputAS.write(output)
    except:
        showError("Write Error!", "Could not write to created .as file.")
        exit()
    

def createASXMLFile(directory, startPath, fileName):
    output = "package "
    output += getPackagePath(directory, startPath)
    
    output += " {\n\
final public class %s {\n\
    [Embed(source=\"%s.%s\", mimeType=\"application/octet-stream\")]\n\
    private static const EmbeddedXML:Class;\n\
    public static var %s:XML = XML(new EmbeddedXML());\n\
    }\n}\n" % (fileName[0], fileName[0], fileName[len(fileName)-1], fileName[0])
    
    fileName = ( directory + "/" + fileName[0] + ".as")
    
    asFiles.append(fileName)
    
    outputAS = open(fileName, 'w')
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
    
    

def createContentsFile(htmlFileURL):
    htmlFile = open(htmlFileURL, 'w')
    htmlFile.write("<table border=\"2\">\n<tr><td><b>Object</b></td><td><b>Package Path</b></td></tr>\n")
    return htmlFile

    
def buildLinkerASFile(directory, startDirectory):
    linkerFileName = (directory + "/" + directory.split('/')[len(directory.split('/'))-1] + ".as")
    
    
    linkerFile = open(linkerFileName, 'w')
    contentsFile = createContentsFile(directory + "/" + directory.split('/')[len(directory.split('/'))-1] + ".html")
    
    linkerFile.write("package {\n")
    
    addedObjects = addASFilesToLinkerFile(directory, startDirectory, linkerFile, contentsFile)
    
    linkerFile.write("import flash.display.Sprite;\n\npublic class %s extends Sprite {\n" % directory.split('/')[len(directory.split('/'))-1])
    
    for imageObject in addedObjects:
        linkerFile.write("\t%s;\n" % imageObject)
        
    linkerFile.write("}\n}\n")
    contentsFile.write("</table>")
    
    asFiles.append(linkerFileName)
    
    
def addASFilesToLinkerFile(directory, startDirectory, linkerFile, contentsFile):
    addedObjects = []
    
    for item in asFiles:
        fileItem = item.rsplit('/')
        objectName = fileItem[len(fileItem)-1].rsplit('.')
        addedObjects.append(objectName[0])
        
        currentPath = item.rsplit('/', 1)
        addToImport(currentPath[0], startDirectory, objectName[0], linkerFile, contentsFile)
    
    return addedObjects
    
    
def addToImport(directory, startDirectory, item, linkerFile, contentsFile):
    packagePath = getPackagePath(directory, startDirectory)
    contentsFile.write("<tr><td>%s</td><td>%s</td></tr>\n" % (item, packagePath))
    if (packagePath == ""):
        packageOut = "%s" % item
    else:
        packageOut = ".%s" % item
    packagePath += packageOut 
    linkerFile.write("import %s\n" % packagePath)
    

