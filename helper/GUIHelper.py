from Tkinter import *
from urllib import urlopen, urlretrieve

import os

def newButton(parent, text, funcCall, x, y):
	button = Button(parent, text=text, fg="red", command=funcCall)
	button.grid(row=x, column=y)
	return button 
	
def newEntry(parent, display, x, y):
    entry = Entry(parent)
    entry.grid(row=x, column=y)
    entry.insert(0, display) 
    return entry
 
