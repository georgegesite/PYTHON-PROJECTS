import numpy as np
from pydub import AudioSegment

def encode_audio_to_array(audio_file, output_file):
    try:
        audio = AudioSegment.from_file(audio_file)
        samples = np.array(audio.get_array_of_samples())
        encoded_array = ','.join(map(str, samples))
        with open(output_file, 'w') as outfile:
            outfile.write(encoded_array)
        print(f"Encoded audio array exported to {output_file}!")
    except FileNotFoundError:
        print("File not found!")


# Provide the path to your MP3 audio file
audio_file_path = 'C:/Users/GEORGIE/Downloads/converted2.mp3'
# Provide the desired output file path
output_file_path = 'C:/Users/GEORGIE/Downloads/output.txt'


encode_audio_to_array(audio_file_path, output_file_path)