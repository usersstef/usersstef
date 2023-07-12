# Generate files with incremented names, just copy the script in the same folder with file to copy,
# and in line 15 edit the filename by your needs

import os

seq = input("Enter a string sequence (Ex: 7_ID) to be replaced: ")

counter = 0
path = r"C:\Python\Filename_replacer"
files = [] 
for file_name in os.listdir (path):
    if "1_ID" in file_name:
        old_name = file_name
        new_name = file_name.replace ("1_ID", seq)
        counter += 1
        files.append (new_name)
        os.rename (old_name, new_name)
print (counter)
print (files)
