
import shutil, glob, os

src_file = r"D:/Python/Filename_generator/FCAudio"  # Folder with source files
src = r"D:/Python/Filename_generator"               # Working folder

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
    prefix = input("Enter the file prefix (Ex: 8_): ").strip()
    if prefix[:-1].isdigit() and prefix.endswith("_"):
        break
    else:
        print("\nInvalid prefix format. Use only digits followed by an underscore (e.g., 7_, 8_)\n")

files_to_rename = [f for f in os.listdir(src) if "1_" in f]
counter = 0
for old_name in files_to_rename:
    new_name = old_name.replace("1_", prefix)
    if not os.path.exists(os.path.join(src, new_name)):
        os.rename(os.path.join(src, old_name), os.path.join(src, new_name))
        counter += 1

print(f"\nPrefix changed to {prefix}")
print()

while True:
    try:
        num = int(input("Enter the amount of files to generate: "))
        break
    except ValueError:
        print("\nInvalid input, please enter only digits\n")

template_file = os.path.join(src, f"{prefix}FBank_.wav")   # Check if the template file exists
if not os.path.exists(template_file):
    print(f"\nError: Template file {template_file} not found.")
    exit(1)

for i in range(1, num + 1):
    dest_file = os.path.join(src, f"{prefix}FBank_{i}.wav")
    shutil.copyfile(template_file, dest_file)

print(f"\nThere are {num} files generated in {src} location")