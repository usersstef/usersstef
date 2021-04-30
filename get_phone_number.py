
# The text sample from info.txt file: "First Name 0722 000 111 random text Second Name 0723 222 333"

import re
import sys

sys.stdout = open('D:\Scripts\Python\phone_list.txt', 'w')
file = open('info.txt')
numlist = list()
for line in file:
    phone_number = re.findall('\w+\s\w+\s\d{4}\-\d{3}\-\d{3}', file.read())
    if len(phone_number) > 0:
        numlist.extend(phone_number)
print()
print("Phone numbers are:", *numlist, sep='\n')
print()
sys.stdout.close()




