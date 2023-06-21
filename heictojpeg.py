from PIL import Image
import os
import pyheif

def convert_heic_to_jpeg(heic_file, output_folder):
    heif_file = pyheif.read(heic_file)
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )

    jpeg_file = os.path.join(output_folder, os.path.splitext(os.path.basename(heic_file))[0] + ".jpg")
    image.save(jpeg_file, "JPEG")

    return jpeg_file

def batch_convert_heic_to_jpeg(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)

        if file_name.lower().endswith(".heic"):
            converted_file = convert_heic_to_jpeg(file_path, output_folder)
            print(f"Converted: {file_name} -> {converted_file}")

# Example usage
input_folder = r"G:\Video Presentation\heic"
output_folder = r"G:\Video Presentation\jpeg"

batch_convert_heic_to_jpeg(input_folder, output_folder)
