#!/usr/bin/env python3
# coding = utf-8
''' Copyright by Joy-IT
    Published under Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License
    Commercial use only after permission is requested and granted '''

'''
ads1115 (aka. 'KY-053') Analog Digital Converter(ADC) - Raspberry Pi Python Code Example
    $ i2cdetect -y 1
            0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
        00:                         -- -- -- -- -- -- -- -- 
        10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
        20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
        30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
        40: -- -- -- -- -- -- -- -- 48 -- -- -- -- -- -- -- 
        50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
        60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
        70: -- -- -- -- -- -- -- --                         
    $ 

    $ sudo usermod -aG dialout pi

    $ pip3 install adafruit-blinka
    $ pip3 install lgpio
    $ pip3 install rpi-lgpio
    $ pip3 install adafruit-circuitpython-ads1x15

    $ ./ads115.py
'''
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from   adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C (board.SCL, board.SDA)

# Create the ADC object using the I2C bus (using default address 0x48)
ads = ADS.ADS1115 (i2c)

# Create single-ended input on channels
chan0 = AnalogIn (ads, ADS.P0)
chan1 = AnalogIn (ads, ADS.P1)
chan2 = AnalogIn (ads, ADS.P2)
chan3 = AnalogIn (ads, ADS.P3)

print ("--------View created Python objects----------------")
print (i2c)
print (ads)
print (chan0)
print ("---------------------------------------------------")

while True:
    # 
    print ("channel 0:", "{:> 5} \t {:> 5.3f}".format(chan0.value, chan0.voltage))
    print ("channel 1:", "{:> 5} \t {:> 5.3f}".format(chan1.value, chan1.voltage))
    print ("channel 2:", "{:> 5} \t {:> 5.3f}".format(chan2.value, chan2.voltage))
    print ("channel 3:", "{:> 5} \t {:> 5.3f}".format(chan3.value, chan3.voltage))
    print ("---------------------------------------------------")
    time.sleep (1)