
# The regex matches for '<FirstName> <SecondName> <OptionalName> <OptionalName> (OptionalPhoneNumber | OptionalEmailAddress)'
# Pattern example: 'Name1 Name2 Name3 Name4 0723-111-222 email@address1.com'

import re
import sys

#sys.stdout = open('D:\Scripts\Python\output_list.txt', 'w') # write output in file
file = open('data.txt') # source file
numlist = list()
for line in file:
    pattern = re.findall('\w+\s+\w+\w+ ?\w+ ?(?:(?:\s\d+-\d+-\d+)?\s+[A-Za-z0-9.+_*-]+@[a-z0-9.+_-]+\.[a-z]+|\s\d+-\d+-\d+)', file.read())
    if len(pattern) > 0:
        numlist.extend(pattern)
print()
print("Searched items are:", *numlist, sep ='\n')
print()
#sys.stdout.close()



