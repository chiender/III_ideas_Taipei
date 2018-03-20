#!/usr/bin/env python
#-*- coding:UTF-8 -*-
#file name:pcf8591.py
#board pins；pin 3=SDA；pin 5=SCL
import time
from smbus import SMBus

AIN0=0 #none
AIN1=1 #potentiometer
AIN2=2 #thermistor
AIN3=3 #light dependent resistor
read_pin=AIN1

bus = SMBus(1)
# i2cset -y 1 0x49 0x01
bus.write_byte(0x49,read_pin)

try:
	while True: # do forever
		reading = bus.read_byte(0x49) # read A/D i2cget -y 1 0x49
		vout=(float(reading)*5)/255
		print('Analog '+ str(read_pin)+' reading: '+str(reading))
		print "Voltage= %.1f v" % vout
		time.sleep(2)#sec

except KeyboardInterrupt:
	print ("KeyboardInterrupt")
