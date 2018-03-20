#!/usr/bin/env python
#-*- coding:UTF-8 -*-
#sensor: YF-S201C Flow Meter
#file name : flow_meter_class.py
import RPi.GPIO as GPIO
import time, sys

class flow:
	count = 0
	def __init__(self,pin):
		GPIO.setmode(GPIO.BOARD)
		#pull_up_down = GPIO.PUD_UP->上拉電阻;GPIO.PUD_DOWN->接地訊號
		GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
		#事件觸發,GPIO.RISING->訊號上升,GPIO.FALLING->訊號下降
		GPIO.add_event_detect(pin, GPIO.FALLING, callback=self.countPulse)
		
	def countPulse(self,channel):
		self.count += 1
		
	def read_count(self):#讀取pulse
		return self.count
		
	def read_flow(self):#讀取L/sec,計算一秒內的count pulse
		time.sleep(0)
		#F=5.1*Q流速(L/Min)
		count_sec = self.read_count()
		flow_sec= (count_sec  / 5.1 / 60)
		#print "Entering Water: %.3f Liters" % (flow_sec)
		count_sec = 0
		self.count=0
		time.sleep(1)
		return flow_sec

	

if __name__ == '__main__':
	f=flow(40) # pin 40,GPIO21
	while True:
		water=f.read_flow()
		print "Entering Water: %.3f Liters" % (water)
