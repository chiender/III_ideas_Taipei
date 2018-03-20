#!/usr/bin/env python
#-*- coding:UTF-8 -*-
#file name: ex1_camera.py
from SimpleCV import Camera
try:
	#初始化相機
	cam=Camera(0,{"width":800,"height":600,"exposure":-2})
	#即時顯示
	cam.live()
#Keyboard Interrupt
except KeyboardInterrupt:
	print("keyboardinterrup")
