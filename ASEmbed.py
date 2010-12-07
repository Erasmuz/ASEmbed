#!/usr/bin/env python

import sys
sys.path.append('./helper')

from Tkinter import *
from GUIHelper import *
from ASBuilder import *

class LevelEditor:
    def __init__(self, master):
        #Create the frame's for the different sections of the main window
    	self.windowFrame = Frame(root)
    	self.compilerFrame = Frame(root)
    	self.buildTypeFrame = Frame(root)

        #Create variables to store current selections.
        self.compileType = "SWC"
    	self.buildType = StringVar()
    	self.buildType.set("Image")
    	
    	#Build the GUI
    	self.buildWindow()
    	
    	
    def buildWindow(self):
        #Create all the buttons
        newButton(self.windowFrame, "Build BitmapData", self.buildBitmapData, 0,0)
        newButton(self.windowFrame, "Build Sprite", self.buildSprite, 1,0)
        newButton(self.windowFrame, "Build XML", self.buildXML, 2,0)
        
        #Still needs to do some sort of action. Need to set default
        Radiobutton(self.compilerFrame, text="SWF", variable=self.compileType, value="SWF").grid(row=0, column=0)
        Radiobutton(self.compilerFrame, text="SWC", variable=self.compileType, value="SWC").grid(row=0, column=1)

        #Create the menu of what type of libraries can be created.
        OptionMenu(self.buildTypeFrame, self.buildType, "Image", "XML", "Audio").pack(anchor=W)

        self.compilerFrame.grid(row=0, column=0)
        self.windowFrame.grid(row=1, column = 0)
        self.buildTypeFrame.grid(row=2, column=0)


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
root.title('ASEmbed')
root.geometry("%dx%d%+d%+d" % (350, 250, 0, 0))

app = LevelEditor(root)
root.mainloop()

