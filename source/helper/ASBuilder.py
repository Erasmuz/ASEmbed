from FileWriter import *
from GUIHelper import *
import commands, re, os

############################################################################
# Main process of building the library.  Generate, link, build, and clean-up
############################################################################
def buildLibrary(parentFrame, directory, compileType, buildType, mxmlcPath):
    #Generate all the need .as files with everything embedded.
    generateASFiles(directory, directory, buildType)
    
    #Build an .as file that includes (links) each newly created .as object.
    buildLinkerASFile(directory, directory)
    
    #Compile the .as files using mxmlc. (or comp)
    flexBuild(directory, compileType, mxmlcPath)
    
    #Clean up all the created .as files.
    removeASFiles(directory)
    

############################################################################
# Checks that a name meets the requirements needed by mxmlc.
############################################################################
def checkName(name):
    tokens = re.findall(validName, name)
    if tokens[0] != name:
        showWarning("Naming Error!", ("Name does not meet naming requirements:\n%s" % name))
        return False
    
    return True


##########################################################################
# Checks that a file is of the correct type to embed and the name meets the requirements.
##########################################################################
def checkFile(buildType, correctType, extension, correctExt, fileName):
    if buildType == correctType and extension in correctExt:
        if checkName(fileName[0]):
            return True
    return False
    

############################################################################
# Recusively scans a directory and generates .as files for files that can be embedded.
############################################################################
def generateASFiles(directory, startPath, buildType):
    #Get the current directory listing.
    dirList = os.listdir(directory)
    
    #Check each item in the current directory.
    for item in dirList:
        currentPath = (directory + "/" + item)
        
        #Directory: Recurse.
        if os.path.isdir(currentPath):
            generateASFiles(currentPath, startPath, buildType)
            
        #File: Check if it's an appropriate type to embed, and do so if needed,.
        else:
            fileName = item.rsplit('.')
            extension = fileName[len(fileName) - 1]
            
            #Chack the extension is a media type that can be embedded.
            if checkFile(buildType, "BitmapData", extension, bitmapTypes, fileName):
                createASBitmapFile(directory, startPath, fileName)
            
            elif checkFile(buildType, "Sprite", extension, spriteTypes, fileName):
                createASSpriteFile(directory, startPath, fileName)
                
            elif checkFile(buildType, "Audio", extension, audioTypes, fileName):
                createASAudioFile(directory, startPath, fileName)
                
            elif checkFile(buildType, "Font", extension, fontTypes, fileName):
                createASFontFile(directory, startPath, fileName)
            
            elif checkFile(buildType, "XML", extension, xmlTypes, fileName):
                createASXMLFile(directory, startPath, fileName)
            
            elif checkFile(buildType, "All", extension, allTypes, fileName):
                if extension in spriteTypes:
                    createASSpriteFile(directory, startPath, fileName)
                elif extension in audioTypes:
                    createASAudioFile(directory, startPath, fileName)
                elif extension in fontTypes:
                    createASFontFile(directory, startPath, fileName)
                elif extension in xmlTypes:
                    createASXMLFile(directory, startPath, fileName)
  
  
#######################################################
# Build the project by calling mxmlc or compc.
######################################################
def flexBuild(directory, compileType, mxmlcPath):
    base = directory.split('/')[len(directory.split('/'))-1] + ".as"
    mxBase = directory + "/" + base

    if (compileType == "SWC"):
        command = "%scompc -source-path %s -include-sources %s/%s -output '%s/%s.swc'" % (mxmlcPath, directory, directory, base, directory, base.split('.')[0])
    elif (compileType == "SWF"):
        command = "%smxmlc %s -output '%s/%s.swf'" % (mxmlcPath, mxBase, directory, base.split('.')[0])
    else:
        showError("Compiler Error!", "Error in compile type.")
        
    returnCode, consoleOutput = commands.getstatusoutput(command)

    if str(returnCode) == "32512":
        showError("Compiler Error!", "MXMLC/COMPC not found.\nMake sure these are in your environment path.")
    else:
        os.system(command)
    
    
#########################################################
# Removes all the created .as files by ASEmbed.
#########################################################
def removeASFiles(directory):
    #Remove the file from the hard drive.
    for item in asFiles:
        os.remove(item)
    
    #Remove the files from the stack
    for i in range(len(asFiles)):
        asFiles.pop()
    
