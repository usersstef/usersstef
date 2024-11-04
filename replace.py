
# In line 12 & 14 edit the filename by your needs

import os

print()
seq = input("Enter a string sequence to replace with (Ex: 7_ID): ")

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
print(); print("There are", counter, "files renamed")
print(), print (*files, sep = '\n')
