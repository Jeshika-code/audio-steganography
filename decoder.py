# Use wave package (native to Python) for reading the received audio file
from pygame import mixer
mixer.init()
mixer.music.load("song_embedded.wav")
mixer.music.set_volume(0.5)
mixer.music.play()
while True:
    print("Press 'e' to exit")

    ch = input("'e']>>>")
    if ch == "e":
        mixer.music.stop()
        break
import wave
song = wave.open("song_embedded.wav", mode='rb')

# Convert audio to byte array
frame_bytes = bytearray(list(song.readframes(song.getnframes())))

# Extract the LSB of each byte
extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
# Convert byte array back to string
string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
# Cut off at the filler characters
decoded = string.split("###")[0]

# Print the extracted text
print("Decoded secret is "+decoded)
song.close()
