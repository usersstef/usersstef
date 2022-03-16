
# Generate files with incremented names, just copy the script in the same folder with file to copy
# If the script is run from other path, use the absolute path of the file like the below example:
# shutil.copyfile('D:\\Scripts\\Python\\replicate\\53_CBank_.wav','D:\\Scripts\\Python\\replicate\\53_CBank_'+str(i+1)+'.wav')

import shutil

while True:
    try:
        num = int(input("Enter the amount of files to generate: "))
        break;
    except ValueError:
        print(); print ("Invalid input, please enter only digits"); print()

for i in range(num):
    shutil.copyfile('53_CBank_.wav','53_CBank_'+str(i+1)+'.wav')
print(); print ("There are", num, "files generated")
input("")

 
