
import re
import sys

sys.stdout = open('D:\Scripts\Python\output_list.txt', 'w') # output
file = open('info.txt') # input
numlist = list()
for line in file:
    pattern = re.findall('\w+ ?\w+ ?\w+\s+\w+(?:(?:\s\d+-\d+-\d+)?\s+[A-Za-z0-9.+_*-]+@[a-z0-9.+_-]+\.[a-z]+|\s\d+-\d+-\d+)', file.read())  # name + optional phone & email
    if len(pattern) > 0:
        numlist.extend(pattern)
print()
print("Searched items are:", *numlist, sep ='\n')
print()
sys.stdout.close()












