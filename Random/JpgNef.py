import os
import shutil

def separate_files_by_extension(src_folder, dest_folder):
    for root, _, files in os.walk(src_folder):
        for file in files:
            if file.lower().endswith(".nef"):
                src_path = os.path.join(root, file)
                dest_path = os.path.join(dest_folder, "nef_files", file)
                shutil.move(src_path, dest_path)
            elif file.lower().endswith(".jpeg") or file.lower().endswith(".jpg"):
                src_path = os.path.join(root, file)
                dest_path = os.path.join(dest_folder, "jpeg_files", file)
                shutil.move(src_path, dest_path)

if __name__ == "__main__":
    # Replace 'source_folder' and 'destination_folder' with your actual folder paths
    source_folder = "C:\Users\georg\Desktop\Photoshoot\DCIM\100D3500"
    destination_folder = "C:\Users\georg\Desktop\Photoshoot"]

    # Make sure the destination folders exist before running the script
    os.makedirs(os.path.join(destination_folder, "nef_files"), exist_ok=True)
    os.makedirs(os.path.join(destination_folder, "jpeg_files"), exist_ok=True)

    separate_files_by_extension(source_folder, destination_folder)
