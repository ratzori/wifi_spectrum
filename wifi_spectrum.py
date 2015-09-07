#!/usr/bin/python
import sys
import re
from pylab import *

chan_list = []
freq_list = []
sign_list = []
ssid_list = []

chan_re = re.compile(r'Channel:([0-9]+)')
freq_re = re.compile(r'Frequency:([0-9.]+)')
sign_re = re.compile(r'Signal level=([0-9-]+)')
ssid_re = re.compile(r'ESSID:"(.*?)"')

for line in sys.stdin:
    chan_match = chan_re.match(line)
    chan = chan_re.search(line)
    if ( chan ):
        chan_list.append(int(chan.group(1)))

    freq_match = freq_re.match(line)
    freq = freq_re.search(line)
    if ( freq ):
        freq_list.append(float(freq.group(1)))

    sign_match = sign_re.match(line)
    sign = sign_re.search(line)
    if ( sign ):
        sign_list.append(int(sign.group(1)))

    ssid_match = ssid_re.match(line)
    ssid = ssid_re.search(line)
    if ( ssid ):
        ssid_list.append(ssid.group(1))

print ("Wi-Fi spectrum analyzer")
print ("SSID:", ssid_list)
print ("Channels:", chan_list)
print ("Frequencies:", freq_list)
print ("Signal dBm:", sign_list)

for i in range(len(freq_list)):
    t = arange(freq_list[i]-0.011, freq_list[i]+0.011, 0.001)
    s = -100000*(t-(freq_list[i]-0.011))*(t-(freq_list[i]+0.011)) + sign_list[i] -12
    plot(t, s)

xlabel('GHz')
ylabel('dBm')
title('Wi-Fi spectrum analyzer')
grid(True)
savefig("spectrum.png")
show()
