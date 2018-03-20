#!/usr/bin/env python
#-*- coding:UTF-8 -*-
#file name: ex2.py
from SimpleCV import Camera, Display, Image
import time
cam=Camera(0,{"width":800,"height":600,"exposure":-2})	#初始化相機
display=Display()	#初始化螢幕顯示
img=cam.getImage()	#從相機擷取一張照片
img.save(display)	#影像顯示在螢幕上
time.sleep(5)

exit()
