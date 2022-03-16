
# The script pars data for final result from a string like 'Dec 31, Doom 3: BFG Edition  5.99'; only 5.99 value is extracted

import re
file = open('SteamAllGames.txt')

numlist = list()
for line in file:
    line_list = re.findall('\d*?\.\d+', file.read())
    if len(line_list) > 0:
        numlist.extend(line_list)
print(numlist)

total = 0
for sum in numlist:
    total += float(sum)
print()	
print("The sum of all steam games is: ", total)



