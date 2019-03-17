"""
1. Read file +
2. Editing wav
3. Export edited
4. Make gui
5. Connect gui + program
6. Look how to start music from time +
7. Saving music when changing, and playing from that time
"""

import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import read
import tkinter

(rate, data) = read('new.wav', 'rb')

print ("Rate "+str(rate))
print ("Length of wav file(in s) = " + str(data.shape[0]/rate))


print(data)

sd.play(data)

sd.wait()


