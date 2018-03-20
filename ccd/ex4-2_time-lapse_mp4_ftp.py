#!/usr/bin/env python
#-*- coding:UTF-8 -*-
#file name: ex4-2_time-lapse_gif.py
import ftplib
import socket 
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
system('ffmpeg -framerate 2 -start_number 0 -i image-%03d.jpg -c:v libx264 -vf fps=30 -pix_fmt yuv420p -y /var/www/html/image-003.mp4')


Host='219.87.162.228' #遠端主機位址
login_account='chander' #登入帳號
login_password='aidsabcgod' #登入密碼
host_path='/chander-pic' #遠端目錄
local_path='/var/www/html/' #本機目錄
local_filename1 = "image-003.mp4" #本機上傳檔名
#local_filename2 = "image-002.jpg" #本機上傳檔名
#local_filename3 = "image-003.jpg" #本機上傳檔名
bufsize=1024 #設定緩衝區大小



try:
	ftp = ftplib.FTP(Host)
	try:
		ftp.login(login_account, login_password)
		print (ftp.getwelcome()) #登入訊息
		try:
			ftp.cwd(host_path) #切換遠端目錄
			print ('遠端:'+ftp.pwd())
			command='STOR '+local_filename1
			filehankler=open(local_path+local_filename1, 'rb')
			ftp.storbinary(command, filehankler, bufsize) #上傳
			print('本機:'+local_path+local_filename1+' 上傳成功')
			
			# command='STOR '+local_filename2
			# filehankler=open(local_path+local_filename2, 'rb')
			# ftp.storbinary(command, filehankler, bufsize) #上傳
			# print('本機:'+local_path+local_filename2+' 上傳成功')
			
			# command='STOR '+local_filename3
			# filehankler=open(local_path+local_filename3, 'rb')
			# ftp.storbinary(command, filehankler, bufsize) #上傳
			# print('本機:'+local_path+local_filename3+' 上傳成功')
			
			ftp.quit()
			exit()
		except (ftplib.error_perm):
			print 'ERROR:遠端目錄不存在' 
			ftp.quit()
			exit()
	except (ftplib.error_perm):
		print 'ERROR:無法登入,請檢查帳號或密碼' 
		ftp.quit()
		exit()
except(socket.error, socket.gaierror): 
	print 'ERROR:無法連線 " %s"' % Host
	exit()

