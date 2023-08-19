import numpy as np
from pydub import AudioSegment

def mp3_to_sound_array(mp3_file):
    # Load the MP3 file
    audio = AudioSegment.from_mp3(mp3_file)

    # Convert the audio to raw PCM data
    raw_data = audio.raw_data

    # Convert raw data to a numpy array
    sound_array = np.frombuffer(raw_data, dtype=np.int16)

    return sound_array

def encode_as_c_array(sound_array, array_name):
    c_array = f"const int16_t {array_name}[] PROGMEM = {{\n"

    for i, sample in enumerate(sound_array):
        c_array += str(sample)
        if i != len(sound_array) - 1:
            c_array += ", "

        if (i + 1) % 16 == 0:
            c_array += "\n"

    c_array += "};"

    return c_array

# Example usage
mp3_file = "converted2.mp3"  # Replace with your own MP3 file
sound_array = mp3_to_sound_array(mp3_file)
c_array = encode_as_c_array(sound_array, "my_sound_array")

print(c_array)
