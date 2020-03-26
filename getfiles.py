
## Get list for specific or all files in current directory and subdirectories

import os, sys
from os import listdir
from os.path import isfile, join

sys.stdout = open('D:\\miscellaneous\\__scripts\\python\\Radio_2000-2002.txt', 'w') # output file
path = 'D:\musica\My_music\Radio 2000 - 2002' # source path

## Parser to list all files name from all subdirectories

files = []
for r, d, f in os.walk(path):
    for file in f:
        if '.' in file:
            files.append(os.path.join(file))
        #if '.py' in file: # 2nd "if" can be used to pars 2 different types of file, can be added as many
            #files.append(os.path.join(file))
print()		
for f in files:
    print(f)
sys.stdout.close()

## Parser to list folders/files name only in the current directory
'''
def getListOfFiles(path): 
    listOfFile = os.listdir(path) # create a list of file and sub directories & names in the given directory
    allFiles = list()
    for entry in listOfFile: # Iterate over all the entries
        # fullPath = os.path.join(path, entry) # Create full path
        fullPath = os.path.join(entry)
        if os.path.isdir(fullPath): # If entry is a directory then get the list of files in this directory
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath) 
    return allFiles
listOfFiles = getListOfFiles(path) 
for f in listOfFiles:
    print(f)
sys.stdout.close()
'''
