#!/usr/bin/env python

import sys
sys.path.append('./helper')

from Tkinter import *
from GUIHelper import *
from ASBuilder import *

class LevelEditor:
    def __init__(self, master):
        #Create the frame's for the different sections of the main window
    	self.tolalFrame = Frame(root)
    	self.menubar = Menu(root)

        self.windowFrame = Frame(root)
    	self.compilerFrame = Frame(root)
    	self.buildTypeFrame = Frame(root)
    	self.directoryFrame = Frame(root)
    	self.goFrame = Frame(root)
    	
        #Create variables to store current selections.
        self.compileType = StringVar()
        self.compileType.set("SWC")
    	self.buildType = StringVar()
    	self.buildType.set("Sprite")
    	self.directory = os.getcwd()
    	self.mxmlcPath = ""
    	
        #Build the GUI
    	self.buildWindow()
    	
    	
    def buildWindow(self):
        #Add menu to the application
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Set MXMLC", command=self.setMXMLC)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=root.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        root.config(menu=self.menubar)
        
        #Still needs to do some sort of action. Need to set default
        label = Label(self.compilerFrame, text="Compile To: ", width=10, height=3).grid(row=0)

        Radiobutton(self.compilerFrame, text="SWC", variable=self.compileType, value="SWC", width=4, relief=RAISED).grid(row=0, column=1)
        Radiobutton(self.compilerFrame, text="SWF", variable=self.compileType, value="SWF", width=4, relief=RAISED).grid(row=0, column=2)
        
        #Create the menu of what type of libraries can be created.
        label = Label(self.buildTypeFrame, text="Object Types: ", width=10).grid(row=0)
        optionmenu = OptionMenu(self.buildTypeFrame, self.buildType, "Sprite", "BitmapData", "XML", "Audio")
        optionmenu.grid(row=0, column=1)
        optionmenu["width"] = 10

        self.directoryBox = newEntry(self.directoryFrame, self.directory, 0, 0)
        
        newButton(self.directoryFrame, "Choose Dir", self.getDirectory, 0,1)
        newButton(self.goFrame, "GO!", self.go, 0,0)
        
        self.compilerFrame.pack()
        self.windowFrame.pack()
        self.buildTypeFrame.pack()
        self.directoryFrame.pack(pady=20)
        self.goFrame.pack()
        
    def setMXMLC(self):
        self.mxmlcPath = tkFileDialog.askdirectory()
        self.mxmlcPath += "/"
        
    def go(self):
        #Test the directory for existance
        try:
            os.listdir(self.directory)
        except:
            showError("Directory Error!", "Directory does not exist:\n%s" % self.directory)
        
        buildLibrary(self.directory, self.compileType.get(), self.buildType.get(), self.mxmlcPath)
        
    
    def getDirectory(self):
        self.directory = tkFileDialog.askdirectory()
        self.directoryBox.delete(0, END)
        self.directoryBox.insert(0, self.directory)
        
        
root = Tk()
root.title('ASEmbed')
root.geometry("%dx%d%+d%+d" % (350, 200, 0, 0))

app = LevelEditor(root)
root.mainloop()

