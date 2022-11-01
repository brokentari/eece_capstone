import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft

start_time = 0
end_time = 10
sample_rate = 500
time = np.arange(start_time, end_time, 1/sample_rate)
theta = 0
frequency = 30
amplitude = 1
sinewave = np.sin(2 * np.pi * frequency * time)

fft_sinewave = np.fft.fft(sinewave)
psd = np.abs(fft_sinewave)
trange = np.linspace(0, sample_rate, len(time))

plt.plot(trange, fft_sinewave)


plt.show()
