# Wi-Fi spectrum usage analyzer
This is a very simple Wi-Fi spectrum usage analyzer for Linux.
Results are generated from the center frequency got from iwlist and bandwidth is always assumed to be 22 MHz.

# How to use
Pipe iwlist scan output to the script i.e.
$ sudo iwlist wlan0 scan|./wifi_spectrum.py

# Depencies
Pylab ( matplotlib )
