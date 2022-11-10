import matplotlib.pyplot as plt
import numpy as np

import pandas as pd
from scipy import signal
import scipy.fftpack


def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = signal.butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)

    y = signal.lfilter(b, a, data)

    return y


sampling_frequency = 1000
duration = 1.5

time = np.arange(0, duration, 1/sampling_frequency)

# signal with 10Hz and 25Hz componenets
y_clean = np.sin(2*np.pi*10*time)
y_noisy = y_clean + 0.1 * \
    np.sin(2*np.pi*60*time) + 0.2 * np.random.normal(size=len(time))

y_filtered = butter_bandpass_filter(y_noisy, 1, 40, 1000)

plt.figure(2)
plt.clf()

plt.plot(time, y_clean)
plt.plot(time, y_filtered)

plt.xlabel('sample(n)')
plt.ylabel('voltage(V)')


plt.show()
