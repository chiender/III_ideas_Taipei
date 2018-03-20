#!/usr/bin/env python
#-*- coding:UTF-8 -*-
#file name : use_flow_class.py
import time, sys
import RPi.GPIO as GPIO
#read class
import flow_meter_class as flow
#pin 40 GPIO21
flow_meter=flow.flow(40)
while True:
	try:
		water=flow_meter.read_flow()
		print "Entering Water: %.3f Liters" % (water)
		
	except KeyboardInterrupt:
		GPIO.cleanup()
		exit()