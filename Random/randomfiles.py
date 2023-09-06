from random import sample
import os

folder = r"G:\Video Presentation\merged2"
items = list(range(1, 400))
x = sample(items, len(items))

for count, filename in enumerate(os.listdir(folder)):
    name, extension = os.path.splitext(filename)

    if extension.lower() in ['.mp4', '.avi', '.mov']:
        new_extension = '.mp4'
    elif extension.lower() in ['.jpg', '.jpeg', '.png']:
        new_extension = '.jpg'
    else:
        continue

    dst = f"{str(x[count])}{new_extension}"
    src = os.path.join(folder, filename)
    dst = os.path.join(folder, dst)

    if os.path.exists(dst):
        print(f"Destination file {dst} already exists. Skipping...")
    else:
        os.rename(src, dst)

print(x)
