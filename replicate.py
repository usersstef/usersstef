
# The script renames incremental a file in a given range

import shutil

for i in range(50):
    shutil.copyfile('D:\\Scripts\\Python\\replicate\\AudioFile_.wav','D:\\Scripts\\Python\\replicate\\AudioFile_'+str(i+1)+'.wav')

 
