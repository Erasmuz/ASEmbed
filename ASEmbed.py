#!/usr/bin/env python

import sys
sys.path.append('./helper')

from Tkinter import *
from GUIHelper import *
from ASBuilder import *

class LevelEditor:
    def __init__(self, master):
    	self.windowFrame = Frame(root)
    	
    	self.buildWindow()
    	
    def buildWindow(self):
        newButton(self.windowFrame, "Build BitmapData", self.buildBitmapData, 0,0)
        newButton(self.windowFrame, "Build Sprite", self.buildSprite, 1,0)
        newButton(self.windowFrame, "Build XML", self.buildXML, 2,0)
        
        self.windowFrame.grid(row=0, column = 0)
    
    def buildBitmapData(self):
        directory = tkFileDialog.askdirectory()
        generateASBitmapFiles(directory, directory)
        buildLinkerASFile(directory, directory)
        flexBuild(directory)
        removeASFiles(directory)
        
    def buildSprite(self):
        directory = tkFileDialog.askdirectory()
        generateASSpriteFiles(directory, directory)
        buildLinkerASFile(directory, directory)
        flexBuild(directory)
        removeASFiles(directory)
        
    def buildXML(self):
        directory = tkFileDialog.askdirectory()
        generateASXMLFiles(directory, directory)
        buildLinkerASFile(directory, directory)
        flexBuild(directory)
        removeASFiles(directory)
        
        
        
root = Tk()
root.geometry("%dx%d%+d%+d" % (250, 150, 0, 0))

app = LevelEditor(root)
root.mainloop()

