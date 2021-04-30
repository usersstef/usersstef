
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

