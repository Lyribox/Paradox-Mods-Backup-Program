# Importing required libraries
import shutil # For copying
import errno # For error tracking
import fileinput # For editing files
import os # For processing files and folders
import re # For editing strings

####################################################
##                                                ##
# Copying all mods from workshop to documents mods #
##                                                ##
####################################################

# Source path for initial backup
backupSrc = "D:/Steam/steamapps/workshop/content/281990"

# Destination path for initial backup
backupDst = "C:/Users/leemu/OneDrive/Documents/Paradox Interactive/Stellaris/mod/backup"

# Copying the Folder and subfolders and files
try:
    shutil.copytree(backupSrc, backupDst)
except OSError as err:
    # Not a directory but a file
    if err.errno == errno.ENOTDIR:
        shutil.copy2(backupSrc, backupDst)
    else:
        print("Source is " + backupSrc + "\n")
        print("Error is " + err.errno)

# Report on copying
print("Copying complete!!\n")


####################################################
##                                                ##
# After backup, format all the mods for use as     #
# local mods by creating descriptor and updating   #
##                                                ##
####################################################

# Backup folder path
descriptorDst = "C:/Users/leemu/OneDrive/Documents/Paradox Interactive/Stellaris/mod/backup"

# Descriptor file path for editing and renaming
descrfile = "C:/Users/leemu/OneDrive/Documents/Paradox Interactive/Stellaris/mod/backup/descriptor.mod"

# For loop to iterate over every folder in the folder to perform the entire operation
for filename in os.listdir(descriptorDst):
    # Variable to store path of the folder being iterated
    modFolder = (os.path.join(descriptorDst, filename)).replace('\\', '/')
    # Variable for path to descriptor in the mod folder for copying
    descrInMod = modFolder + "/descriptor.mod"

    # Copy the descriptor file in the parent backup folder
    shutil.copy2(descrInMod, descriptorDst)

    # Load the current descriptor to begin editing
    with fileinput.FileInput(descrfile, inplace = True, backup ='.bak') as f:
        # Iterating line by line to find the name and remote line
        for line in f:
            # Finds remote id line and replaces it with the path directory
            if "remote" in line:
                print('path="' + newPath + '"', end="\n")

            # Finds name of the mod and creates variables for use in operation
            elif "name=" in line:
                print(line, end='')
                start = line.index('"')
                end = line.index('"', start+1)
                modName = re.sub(r'\W+', '_', (line[start+1:end]))
                newPath = descriptorDst + '/' + modName
                newDescrPath = newPath + '.mod'
            else:
                print(line, end='')

    # Rename the descriptor and mod number folder to actual mod name
    for retry in range(100):
        try:
            os.rename(descrfile, newDescrPath)
            os.rename(modFolder, newPath)
            break
        except:
            print("rename failed, retrying...")
    
    # Report on backing up
    if not(os.path.isfile(modFolder)):
        print(modName + ' backed up!!!')

####################################################
##                                                ##
# MODS ARE OFFICIALLY BACKED UP                    #
##                                                ##
####################################################