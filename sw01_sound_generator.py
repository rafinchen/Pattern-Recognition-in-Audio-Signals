import numpy as np
import pyaudio

p = pyaudio.PyAudio()

volume = 0.6
fs = 44100
duration = 5.0

t = np.arange(int(fs * duration)) / fs
freq1 = 440.0
freq2 = 660.0
modulator = 0.5 * np.sin(2 * np.pi * 2.0 * t) + 0.5

samples = (
    (np.sin(2 * np.pi * freq1 * t) +
     0.5 * np.sin(2 * np.pi * freq2 * t)) *
    modulator +
    0.1 * np.random.randn(len(t))
).astype(np.float32)

stream = p.open(format=pyaudio.paFloat32, channels=1, rate=fs, output=True)
stream.write((volume * samples).tobytes())
stream.stop_stream()
stream.close()
p.terminate()
