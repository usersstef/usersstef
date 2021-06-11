
# Generate files with incremented names, just copy the script in the same folder with file to copy
# If the script is run from other path, use the absolute path of the file like the below example:
# shutil.copyfile('D:\\Scripts\\Python\\replicate\\53_CBank_.wav','D:\\Scripts\\Python\\replicate\\53_CBank_'+str(i+1)+'.wav')

import shutil

for i in range(10):
    shutil.copyfile('53_CBank_.wav','53_CBank_'+str(i+1)+'.wav')

 
