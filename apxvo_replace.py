
import shutil, glob, os

file_src = r"D:/Python/Filename_replacer/ApexVO"   # Apex VO file path
src = r"D:/Python/Filename_replacer"
dst = r"//mad-fs1/IDS/Engineering/QATeam/Stef1"

files = glob.iglob(os.path.join(file_src, "*.wav"))
for file in files:
    if os.path.isfile(file):
        shutil.copy2(file, src)

print()
prefix = input("Enter the file prefix (Ex: 7_ID): ")

counter = 0
path = src
files = [] 
for file_name in os.listdir (path):
    if "1_ID" in file_name:
        old_name = file_name
        new_name = file_name.replace ("1_ID", prefix)
        counter += 1
        files.append (new_name)
        os.rename (old_name, new_name)
# print(), print (*files, sep = '\n')

# files = glob.iglob(os.path.join(src, "*.wav"))
# for file in files:
#     if os.path.isfile(file):
#         shutil.move(file, dst)

print(); print("There are", counter, "files renamed and copied to", dst, "location")

