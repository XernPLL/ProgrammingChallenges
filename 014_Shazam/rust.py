from pyAudioAnalysis import audioTrainTest as aT
import queue
import os
import sys
import time
import sounddevice as sd
import soundfile as sf
import numpy  # Make sure NumPy is loaded before it is used in the callback
assert numpy  # avoid "imported but unused" message (W0611)
from fbchat import Client
from fbchat.models import *
import shutil
try:
    shutil.rmtree('sciezki', ignore_errors=True)
except:
    pass
try:
    os.mkdir("sciezki")
except:
    pass
client = Client('e-mail', 'password')
q = queue.Queue()
ficzery=["cisza","alarm","rakietybaza","rakietydaleko","tlumik", "ak", "c4", "c4dalej","statek", "helka"]
aT.featureAndTrain(ficzery, 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svmSMtemp", False)

def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy())

device_info = sd.query_devices(2, 'input')
samplerate = int(device_info['default_samplerate'])
i=0
try:
    while(True):
        with sf.SoundFile("sciezki/output{}.wav".format(i), mode='x', samplerate=samplerate,
                          channels=2) as file:
            with sd.InputStream(samplerate=samplerate, device=2,
                                channels=2, callback=callback):
                czas = time.time()
                while (time.time()-czas)<=5:
                    file.write(q.get())

        wynik = aT.fileClassification("sciezki/output{}.wav".format(i), "svmSMtemp","svm")

        klasyfikacja = ficzery[int(wynik[0])]
        if wynik[1][0] < 0.5:
            print(klasyfikacja)
            print(i)
        if klasyfikacja == "alarm" or klasyfikacja == "rakietybaza" or klasyfikacja == "c4" or klasyfikacja == "tlumik" or klasyfikacja == "statek"or klasyfikacja == "helka":
            client.send(Message(text=klasyfikacja), thread_id='ID', thread_type=ThreadType.GROUP)
            pass
        i = i+1




except KeyboardInterrupt:
    client.send(Message(text="End Detect"), thread_id='ID', thread_type=ThreadType.GROUP)
    client.logout()


