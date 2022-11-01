import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
import numpy as np
import scipy.fftpack
import matplotlib.pyplot as plt

x=0
data = pd.read_csv('ads_eeg_data')
data = data['voltage']

print(data)

dataset_y=[]
dataset_x=[]
for a in data:  
          dataset_y.append(float(a))
          x=x+1
          dataset_x.append(x)


print(len(dataset_x))
print(len(dataset_y))

def butter_highpass(cutoff, fs, order=3):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='high', analog=False)
    return b, a

def butter_highpass_filter(data, cutoff, fs, order=5):
    b, a = butter_highpass(cutoff_high, fs, order=order)
    y = signal.filtfilt(b, a, data)
    return y

def butter_lowpass(cutoff, fs, order=4):   
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=4):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = signal.lfilter(b, a, data)    
    return y

fps = 500
cutoff_high=1
cutoff_low=40

filtered_sine_high = butter_highpass_filter(dataset_y, cutoff_high, fps)
filtered_sine_low =  butter_lowpass_filter(dataset_y, cutoff_low, fps)
filtered_high_pass= butter_lowpass_filter(filtered_sine_high, cutoff_low, fps)#[5000:15000]

samplingFrequency   = 500 
beginTime           = 0;
endTime             = int(len(filtered_high_pass)/samplingFrequency); 
time  = np.arange(0, (len(filtered_high_pass)/samplingFrequency),1/samplingFrequency);


figure, axis = plt.subplots(3, 1)
plt.subplots_adjust(hspace=1)
axis[0].set_title('Data after pass filter')
axis[0].plot(time, filtered_high_pass)
axis[0].set_xlabel('Time')
#axis[0].set_xlim([5, 15])
axis[0].set_ylabel('Amplitude')


# Frequency domain representation
fourierTransform = np.fft.fft(filtered_high_pass)/len(filtered_high_pass)           # Normalize amplitude
fourierTransform = fourierTransform[range(int(len(filtered_high_pass)/2))] # Exclude sampling frequency
tpCount     = len(filtered_high_pass)
values      = np.arange(int(tpCount/2))

timePeriod  = tpCount/samplingFrequency
print ("tpCount",tpCount)
print ("samplingFrequency",samplingFrequency)
print ("timePeriod",timePeriod)

frequencies = values/timePeriod
axis[1].set_title('Fourier transform depicting the frequency components')
axis[1].plot(frequencies, abs(fourierTransform))
axis[1].set_xlabel('Frequency')
axis[1].set_ylabel('Amplitude')


# Power pectral density
psd = np.abs(fourierTransform)
axis[2].set_title('Power Spectral Density')
axis[2].plot(frequencies, np.abs(fourierTransform))
axis[2].set_xlabel('PSD')
axis[2].set_xlabel('Frequency')


plt.show()







