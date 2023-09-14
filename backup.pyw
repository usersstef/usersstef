
import os, sys # Import mod

# Parse & update the tracklist

sys.stdout = open('D:\\Scripts\\Python\\Backup\\Track_list.txt', 'w')
path1 = 'D:\musica\My_music\Chill_step'
files = []
for r, d, f in os.walk(path1):
    for file in f:
        if '.mp3' in file:
            files.append(os.path.join(file))
print()
for f in files:
    print(f)

path2 = 'D:\musica\My_music\Ambiental'
files = []
for r, d, f in os.walk(path2):
    for file in f:
        if '.mp3' in file:
            files.append(os.path.join(file))

# path3 = 'D:\musica\My_music\Radio 2000 - 2002'
# files = []
# for r, d, f in os.walk(path3):
#     for file in f:
#         if '.mp3' in file:
#             files.append(os.path.join(file))
print()
for f in files:
    print(f)
sys.stdout.close()


