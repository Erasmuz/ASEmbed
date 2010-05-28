#!/usr/bin/env python

import sys
sys.path.append('./helper')

from Tkinter import *
from GUIHelper import *

class LevelEditor:
    def __init__(self, master):
    	self.buttons = []
    	self.entries = {}
    	
    	self.windowFrame = Frame(root)
    	
    	self.buildWindow()
    	
    def buildWindow(self):
        self.buttons.append(newButton(self.windowFrame, "?", self.buildBitmapData, 0,0))
        self.buttons.append(newButton(self.windowFrame, "Create Spawn", self.buildSprite, 1,0))
        self.buttons.append(newButton(self.windowFrame, "ReBuild", self.buildXML, 3,0))
        
        self.windowFrame.grid(row=0, column = 0)
    
    def buildBitmapData(self):
        print "test" 
        
    def buildSprite(self):
        print "test"
        
        
    def buildXML(self):
        print "test"
   
   
root = Tk()
root.geometry("%dx%d%+d%+d" % (250, 150, 0, 0))
app = LevelEditor(root)

root.mainloop()

