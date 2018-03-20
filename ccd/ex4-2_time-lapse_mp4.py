#!/usr/bin/env python
#-*- coding:UTF-8 -*-
#file name: ex4-2_time-lapse_gif.py
from SimpleCV import Camera,Image,Color
from os import system
import time
from datetime import datetime

cam=Camera(0,{"width":320,"height":240})	#640X480
numFrames=15	#拍照張數
img=cam.getImage()
time.sleep(3)
for x in range(0,numFrames):
	now2=str(datetime.now()) #顯示現在時間
	img=cam.getImage()
	#image-000.jpg,image-001.jpg
	filepath="image-{0:03d}.jpg".format(x)
	img.drawText(now2,30,220,Color.RED,30)
	img.save(filepath)
	print "Saved image to:"+filepath
	time.sleep(3)	#每3秒一張
#自動轉換成GIF檔
#system('convert -delay 30 -loop 0 image-*.jpg -resize 160x120 mypic.gif')

#自動轉換成mp4檔,image-001.jpg
system('ffmpeg -framerate 2 -start_number 0 -i image-%03d.jpg -c:v libx264 -vf fps=30 -pix_fmt yuv420p -y /var/www/html/mp4out.mp4')
