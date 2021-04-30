
# The text sample from info.txt file: "First Name 0722 000 111 random text Second Name 0723 222 333"

import re
import sys

sys.stdout = open('D:\Scripts\Python\phone_list.txt', 'w') # output
file = open('info.txt') # input
numlist = list()
for line in file:
    pattern = re.findall('\w+\s\w+\s\d{4}\-\d{3}\-\d{3}', file.read()) # regex
    if len(pattern) > 0:
        numlist.extend(pattern)
print()
print("Phone numbers are:", *numlist, sep='\n')
print()
sys.stdout.close()




