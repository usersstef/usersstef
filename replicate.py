
# Generate files with incremented names
# Copy the script in the same folder with file to copy

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

 
