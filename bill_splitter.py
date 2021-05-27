
# The script extracts data for final result from a string like '01, 30.5' where 01 is the date and 30.5 is the price; only 30.5 value is parsed

import re

file = open('shopping_list.txt')
numlist = list()
for line in file:
    line_list = re.findall('\d*?\.\d+', file.read())
    if len(line_list) > 0:
        numlist.extend(line_list)
print();print("All the common costs until now:", numlist);print()
print("*************************************");print()

total = 0
for sum in numlist:
    total += float(sum)
print("The common Total until now:    ", total);print();print("The common Total divided on 3: ", float(total/3))
print();input(" ")

