import os
from PIL import Image

def get_image_orientation(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
        if width > height:
            return 'landscape'
        elif width < height:
            return 'portrait'
        else:
            return 'square'

def sort_images_and_videos(directory):
    landscape_folder = os.path.join(directory, 'landscape')
    portrait_folder = os.path.join(directory, 'portrait')

    # Create folders if they don't exist
    if not os.path.exists(landscape_folder):
        os.makedirs(landscape_folder)
    if not os.path.exists(portrait_folder):
        os.makedirs(portrait_folder)

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                orientation = get_image_orientation(file_path)
                if orientation == 'landscape':
                    destination_folder = landscape_folder
                else:
                    destination_folder = portrait_folder
                os.rename(file_path, os.path.join(destination_folder, file))
            elif file.lower().endswith(('.mp4', '.mov', '.avi')):
                destination_folder = landscape_folder  # Assuming videos are always landscape
                os.rename(file_path, os.path.join(destination_folder, file))

# Specify the directory containing the images and videos
directory = r'G:\Video Presentation\fddon22'

sort_images_and_videos(directory)
