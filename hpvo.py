
import shutil, glob, os

src_file = r"D:/Python/Filename_generator/HopperVO"  # Folder with source files
src = r"D:/Python/Filename_generator"                # Working folder

for wav_file in glob.glob(os.path.join(src, "*.wav")):   # Remove .wav files from working folder
    try:
        os.remove(wav_file)
    except Exception as e:
        print(f"Could not delete {wav_file}: {e}")

files = glob.iglob(os.path.join(src_file, "*.wav"))   # Copy .wav file from src_file to src
for file in files:
    if os.path.isfile(file):
        shutil.copy2(file, src)
print()

while True:
    try:
        num = int(input("Enter the amount of files to generate: "))
        break
    except ValueError:
        print()
        print("Invalid input, please enter only digits")
        print()

wav_files = [f for f in os.listdir(src) if f.endswith('.wav')]   # Get the first .wav file from src to use as the source for copies
if not wav_files:
    print("No .wav files found in the src folder:", src)
    exit()

source_file = os.path.join(src, wav_files[0])  # first found .wav file

for i in range(1, num + 1):
    number_part = f"{i:07d}"
    new_filename = f"{number_part}_HOSTESS_FRE_FR.wav"
    dst_path = os.path.join(src, new_filename)
    shutil.copyfile(source_file, dst_path)

print()
print("There are", num, "files generated in", src, "location")