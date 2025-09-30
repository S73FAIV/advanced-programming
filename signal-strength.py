####
# The tranlated exercise (by deepl.com):
#
# In the ‘intensity’ file, we have a record of the wireless connection signal strength on a series of devices that are being monitored minute by minute. 
# Each line shows the signal strength on each device on a scale of 0 to 5. 
# We are interested in the time that a device is continuously without a signal, that is, we look at how long it takes to recover the signal. 
# 
# Write a programme that asks on screen how many devices there are and writes which device has been without a signal for the longest continuous period of time, 
# i.e. locate the longest period without a signal and say which device it was. 
# 
# You must use a function other than main, dividing the work into similar parts and passing arguments.

# Examples
# If the record is as follows:
# 1 2 3
# 0 3 2
# 3 1 3
# 1 0 0
# 0 0 2
# 5 2 0
# 4 4 2
# 5 3 0
# 0 2 3
# We see that the longest period without a signal was 2 minutes and it was on the second device 
# (the first, for example, was without a signal for three minutes, but not consecutively). 
# Therefore, the solution would be 2.
####

import numpy as np

signal_data = np.loadtxt(fname="intensity.txt")

current_outage_time = 1
current_longest_outage_time = 0
current_device_longest_offline = -1

# We Loop per device (equals column in the txt-file)
for column in range(len(signal_data[0,:])):
    # We loop over all entries
    for minute in range(len(signal_data[:,column])):
        current_signal = signal_data[minute, column]
        # if the signal andthe signal bevore are an outage -> count
        if current_signal == 0 and signal_data[(minute-1), column] == 0:
            current_outage_time += 1
            if current_outage_time > current_longest_outage_time:
                current_longest_outage_time = current_outage_time
                current_device_longest_offline = column
        else:
            current_outage_time = 1
        


print("Longest Outage:", current_longest_outage_time)
print("Device Missing:", current_device_longest_offline)
