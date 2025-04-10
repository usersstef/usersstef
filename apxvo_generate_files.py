
# Generate files with incremented names, just copy the script in the same folder with file to copy,
# and in for loop edit the filename by your needs

import shutil, glob, os

file_src = r"D:/Python/Filename_generator/ApexVO"  # Apex VO file path
src = r"D:/Python/Filename_generator"
dst = r"//mad-fs1/IDS/Engineering/QATeam/Stef1"

files = glob.iglob(os.path.join(file_src, "*.wav"))
for file in files:
    if os.path.isfile(file):
        shutil.copy2(file, src)

print()
prefix = input("Enter the file prefix (Ex: 7_): ")

counter = 0
path = src
files = [] 
for file_name in os.listdir (path):
    if "1_" in file_name:
        old_name = file_name
        new_name = file_name.replace ("1_", prefix)
        counter += 1
        files.append (new_name)
        os.rename (old_name, new_name)

print()
while True:
    try:
        num = int(input("Enter the amount of files to generate: "))
        break
    except ValueError:
        print(); print("Invalid input, please enter only digits"); print()
        # break;

for i in range(num):
    shutil.copyfile(str(prefix)+'ID_GER_DE.wav', str(prefix)+'ID'+str(i+1)+'_GER_DE.wav')

# files = glob.iglob(os.path.join(src, "*.wav"))
# for file in files:
#     if os.path.isfile(file):
#         shutil.move(file, dst)
print()
print("There are", num, "files generated and copied to", dst, "location")
#input("")

