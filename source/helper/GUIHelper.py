from Tkinter import *
from urllib import urlopen, urlretrieve

import webbrowser  
import tkFileDialog
import tkMessageBox
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
 
def displayHelp():
    webbrowser.open("./ASHelp.html")
        
def showError(title='Title', message='your message here.'):
    tkMessageBox.showerror( title, message )
    return
    
def showWarning(title='Title', message='your message here.'):
    tkMessageBox.showwarning( title, message )
    return

def showInfo(title='Title', message='your message here.'):
    tkMessageBox.showinfo( title, message )
    return
    
    
