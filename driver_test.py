#!/usr/bin/python
# -*- coding: utf-8 -*-

from RaspberryPiADS1299 import ADS1299_API
from time import time, sleep
from fft import butter_bandpass_filter
import threading
import time

chunks_processed = 0
result = []
total_samples = 0
chunk_file_threads = []


# Inheriting the base class 'Thread'

class AsyncWrite(threading.Thread):

    def __init__(self, data, out):

        # calling superclass init

        threading.Thread.__init__(self)
        self.out = out
        self.data = data

    def run(self):
        with open(self.out, 'w') as f:
            f.write('\n'.join([str(i) for i in self.data]))

        print ('Finished background file write to', self.out)


def processFFT():
    global chunks_processed
    global chunk_file_threads
    global total_samples

    chunks_processed += 1

    fft_chunk = result.copy()
    result.clear()
    total_samples += len(fft_chunk)
        # print('FFT CHUNK LENGTH: ', len(fft_chunk))
        # print('chunks processed: ', chunks_processed)
        # file_name = 'ads_eeg_data_' + str(chunks_processed)
        # with open(file_name, 'w') as txt_file:
            # for f in fft_chunk:
                    # txt_file.write(f'{f}\n')

        # filtered_signal = butter_bandpass_filter(fft_chunk, 1, 40, 1000)
        # = np.fft.fft(filtered_signal)

    print(chunks_processed)

        # print(filtered_signal)

    out_file = 'ads_eeg_data_' + str(chunks_processed)
    background = AsyncWrite(fft_chunk, out_file)
    chunk_file_threads.append(background)
    background.start()
    return len(fft_chunk)


def proccesPSD(data):
    sleep(1)
    print('psd processed')

    result.clear()
    return 0


def DefaultCallback(data):

    # print(data)

    result.append(data)
    if len(result) == 1000:
        processFFT()


# initialize ADS api

ads = ADS1299_API()

ads.openDevice()
ads.registerClient(DefaultCallback)
ads.configure(sampling_rate=1000, nb_channels=1)

print('ADS1299 API test stream starting')
ads.startEegStream()
sleep(10)
print('ADS1299 API test stream stopping')
ads.stopStream()

# cleanup

ads.closeDevice()
sleep(1)
print('Test Over')

total_samples += len(result)

print('wait for threads to finish')
for t in chunk_file_threads:
    t.join()

# file_name = 'ads_eeg_data_' + str(int(time()))
# print(file_name)
print(f'num of samples: {total_samples}')
print(f'first element: {result[0]}')
print(f'last element: {result[len(result)-1]}')
# with open(file_name, 'w') as txt_file:
#    for f in result:
#        txt_file.write(f'{f}\n')
