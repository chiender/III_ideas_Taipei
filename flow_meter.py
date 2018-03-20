#!/usr/bin/env python
#-*- coding:UTF-8 -*-
#sensor: YF-S201C Flow Meter
#file name : flow_meter.py
import RPi.GPIO as GPIO
import time, sys

FLOW_SENSOR = 40 #輸入腳位
GPIO.setmode(GPIO.BOARD)
#pull_up_down = GPIO.PUD_UP->上拉電阻;GPIO.PUD_DOWN->接地訊號
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP)

global count
global total_count
count = 0
total_flow=0
total_count = 0

def countPulse(channel):
	global count
	global total_count
	count = count+1
	total_count=total_count+1
	#print count
#事件觸發,GPIO.RISING->訊號上升,GPIO.FALLING->訊號下降
GPIO.add_event_detect(FLOW_SENSOR, GPIO.FALLING, callback=countPulse)


while True:
	try:
		#time.sleep(1)
		start_counter = 1
		time.sleep(0)
		start_counter = 0
		#F=5.1*Q流速(L/Min)
		flow= (count / 5.1 / 60)
		print "Entering Water: %.3f Liters" % (flow)
		count = 0
		time.sleep(1)
		#計算總流量
		total_flow=total_flow+flow
	except KeyboardInterrupt:
		print "\ntotal Water: %.3f Liters" % (total_flow)
		print "\ntotal count: %d" % total_count
		GPIO.cleanup()
		sys.exit()