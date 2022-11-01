#!/usr/bin/env python3

from RaspberryPiADS1299 import ADS1299_API
from time import time, sleep
from datetime import datetime

result = []

"""
DefaultCallback
@brief used as default client callback for tests 
@data byte array of 1xN, where N is the number of channels
"""
def DefaultCallback(data):
    result.append(data)

# initialize ADS api
ads = ADS1299_API()

ads.openDevice()
ads.registerClient(DefaultCallback)
ads.configure(sampling_rate=500, nb_channels=1)

print("ADS1299 API test stream starting")
ads.startEegStream()
sleep(10)
print("ADS1299 API test stream stopping")
ads.stopStream()

# cleanup
ads.closeDevice()
sleep(1)
print('Test Over')

print(result)


# Generate the unique filename
dt = datetime.now()
file_name = 'ads_eeg_data_' + str(dt)

with open(file_name, 'w') as txt_file:
    txt_file.write('\n'.join(' '.join(map(str, x)) for x in result))
