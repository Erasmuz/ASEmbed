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
    	self.directoryFrame = Frame(root)
    	self.goFrame = Frame(root)
    	
        #Create variables to store current selections.
        self.compileType = "SWC"
    	self.buildType = StringVar()
    	self.buildType.set("Sprites")
    	self.directory = "/"
    	
#Build the GUI
    	self.buildWindow()
    	
    	
    def buildWindow(self):
        #Still needs to do some sort of action. Need to set default
        Radiobutton(self.compilerFrame, text="SWF", variable=self.compileType, value="SWF").grid(row=0, column=0)
        Radiobutton(self.compilerFrame, text="SWC", variable=self.compileType, value="SWC").grid(row=0, column=1)

        #Create the menu of what type of libraries can be created.
        OptionMenu(self.buildTypeFrame, self.buildType, "Sprites", "Bitmaps", "XML", "Audio").pack(anchor=W)

        self.directoryBox = newEntry(self.directoryFrame, "[Directory]", 0, 0)
        newButton(self.directoryFrame, "Choose Dir", self.getDirectory, 0,1)
        
        newButton(self.goFrame, "GO!", self.go, 0,0)
        
        self.compilerFrame.grid(row=0, column=0)
        self.windowFrame.grid(row=1, column = 0)
        self.buildTypeFrame.grid(row=2, column=0)
        self.directoryFrame.grid(row=3, column=0)
        self.goFrame.grid(row=4, column=0)
        
    def go(self):
        buildLibrary(self.directory, self.compileType, self.buildType.get())
        
        
    def getDirectory(self):
        self.directory = tkFileDialog.askdirectory()
        self.directoryBox.delete(0, END)
        self.directoryBox.insert(0, self.directory)
        
        
root = Tk()
root.title('ASEmbed')
root.geometry("%dx%d%+d%+d" % (350, 250, 0, 0))

app = LevelEditor(root)
root.mainloop()

