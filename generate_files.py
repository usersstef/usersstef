
# Generate files with incremented names, just copy the script in the same folder with file to copy,
# and in for loop edit the filename by your needs

import shutil, glob, os

# file_src = r"D:/Python/Filename_generator/ApexVO"  # Apex VO file path
file_src = r"D:/Python/Filename_generator/FCAudio"  # FC Audio file path
src = r"D:/Python/Filename_generator"
dst = r"//mad-fs1/IDS/Engineering/QATeam/Stef1"

files = glob.iglob(os.path.join(file_src, "*.wav"))
for file in files:
    if os.path.isfile(file):
        shutil.copy2(file, src)

print()
while True:
    try:
        num = int(input("Enter the amount of files to generate: "))
        break
    except ValueError:
        print(); print("Invalid input, please enter only digits"); print()
        # break;

for i in range(num):
	# shutil.copyfile('1_ID_GER_DE.wav','1_ID'+str(i+1)+'_GER_DE.wav')  #  ApexVO format
	shutil.copyfile('1_FBank_.wav','1_FBank_'+str(i+1)+'.wav')         # FC Audio format

#shutil.copyfile(src + filename, dst + filename) # this line is to copy only one file

files = glob.iglob(os.path.join(src, "*.wav"))
for file in files:
    if os.path.isfile(file):
        shutil.move(file, dst)
print()
print("There are", num, "files generated and copied to", dst, "location")
#input("")


