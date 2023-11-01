import wave
import matplotlib.pyplot as plt
import numpy as np
import constant

# Open wav file
obj = wave.open(constant.file_path_recordings + constant.file_name_wav, "rb")

# print("Number of channels:", obj.getnchannels())
# print("Sample width:", obj.getsampwidth())
# print("Frame rate:", obj.getframerate())
# print("Number of frames:", obj.getnframes())
# print("Parameters:", obj.getparams())

# Get needed values from the wav file
sample_freq = obj.getframerate()
n_samples = obj.getnframes()
signal_wave = obj.readframes(-1)

obj.close()

t_audio = n_samples / sample_freq


signal_array = np.frombuffer(signal_wave, dtype=np.int16)
times = np.linspace(0, t_audio, num=n_samples)

# Create plot
plt.figure(figsize=(15,5))
plt.plot(times, signal_array)
plt.title("AUDIO")

plt.xlabel("Time (s)")
plt.ylabel("Signal Wave")

plt.xlim(0, t_audio)
plt.show()