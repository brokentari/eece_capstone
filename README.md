# EECE Capstone

Raspberry Pi 4 scripts (should be ran/modified in Rpi):
- ADS1299_API.py (initializes the ADS1299 and converts read values into voltage)
- driver_test.py (main entry point to start collecting data)

Testing scripts (can be run on any other computer):
 - fft.py (plots the data in the `ads_eeg_data` file)
 - remove_anytime.py (just temp file to test out signal processing)


Workflow:
1. Ensure ADS is turned on and electrodes are placed
2. Run `python driver_test.py` to start collecting data
3. Transfer the generated file into a seperate machine (working on removing this step)
	3a. Windows and Mac have `scp` to transfer the file (type `hostname -I` in Rpi to find Rpi IP addr)
4. Name the file `ads_eeg_data` and run `python fft.py`
