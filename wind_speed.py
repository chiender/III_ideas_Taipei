#!/usr/bin/env python
#-*- coding:UTF-8 -*-
#Davis 7911 wind sensor
#file name : wind_speed.py
import RPi.GPIO as GPIO
import time, sys

FLOW_SENSOR = 40 #輸入腳位
GPIO.setmode(GPIO.BOARD)
#pull_up_down = GPIO.PUD_UP->上拉電阻;GPIO.PUD_DOWN->接地訊號
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP)

global count
count = 0

def countPulse(channel):
	global count
	count = count+1

#事件觸發,GPIO.RISING->訊號上升,GPIO.FALLING->訊號下降
GPIO.add_event_detect(FLOW_SENSOR, GPIO.FALLING, callback=countPulse)

while True:
	try:
		start_counter = 1
		time.sleep(0)
		start_counter = 0
		#風速計算,mph = 2.25 * counts / seconds ,range 2-150
		mph = (count * 2.25)
		#mph轉換為 m/s,m/s range 1~67
		ms=(67 * mph / 150 )
		#mph轉換為 km/h,km/h range 3~241
		#kmh=(241 * mph / 150 )
		#print "Wind Speed: %.3f mph" % (mph)
		print "Wind Speed: %.3f m/s" % (ms)
		#print "Wind Speed: %.3f km/h" % (kmh)
		count = 0
		time.sleep(1) #計算1秒間的count

	except KeyboardInterrupt:
		GPIO.cleanup()
		sys.exit()