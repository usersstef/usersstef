
# Importing modules

import os, sys

# Parse & update the tracklist in the txt file

sys.stdout = open('D:\\Scripts\\Python\\Backup\\Track_list.txt', 'w')
path = 'D:\musica\My_music\Ambiental'
files = []
for r, d, f in os.walk(path):
    for file in f:
        if '.mp3' in file:
            files.append(os.path.join(file))
print()
for f in files:
    print(f)

path1 = 'D:\musica\My_music\Chill_step'
files = []
for r, d, f in os.walk(path1):
    for file in f:
        if '.mp3' in file:
            files.append(os.path.join(file))
print()
for f in files:
    print(f)
sys.stdout.close()


