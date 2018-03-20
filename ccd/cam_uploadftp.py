#!/usr/bin/env python
#-*- coding:UTF-8 -*-
#file name:cam_uploadftp.py
import ftplib
import socket 
from SimpleCV import Camera,Image,Color
#from os import system
import os
import time
from datetime import datetime
print ("try...")
try :
	cam=Camera(0,{"width":320,"height":240})	#320X240
	img=cam.getImage()
	time.sleep(3)
	now2=str(datetime.now()) #顯示現在時間
	img=cam.getImage()
	#image-000.jpg,image-001.jpg,在寫在/var/www/html/下才能存檔
	filepath="/var/www/html/image-001.jpg"
	img.drawText(now2,30,220,Color.RED,30)
	img.save(filepath)
	print ("SAVE:image-001.jpg")

	cam=Camera(1,{"width":320,"height":240})	#320X240
	img=cam.getImage()
	time.sleep(3)
	now2=str(datetime.now()) #顯示現在時間
	img=cam.getImage()
	#image-000.jpg,image-001.jpg
	filepath="/var/www/html/image-002.jpg"
	img.drawText(now2,30,220,Color.RED,30)
	img.save(filepath)
	print ("SAVE:image-002.jpg")

	cam=Camera(2,{"width":320,"height":240})	#320X240
	img=cam.getImage()
	time.sleep(3)
	now2=str(datetime.now()) #顯示現在時間
	img=cam.getImage()
	#image-000.jpg,image-001.jpg
	filepath="/var/www/html/image-003.jpg"
	img.drawText(now2,30,220,Color.RED,30)
	img.save(filepath)
	print ("SAVE:image-003.jpg")

except (IOError,TypeError, AttributeError) as e:
	print ("camera error")
	#像機使用一陣子會出現libv4l2: error setting pixformat: Device or resource busy
	#在AttributeError
	#砍掉python的工作行程即可回復
	#os.system("killall -9 python")
	print ("killall python")
	os.system("sudo reboot")
	print ("reboot")
	exit()

Host='219.87.162.228' #遠端主機位址
login_account='chander' #登入帳號
login_password='aidsabcgod' #登入密碼
host_path='/chander-pic' #遠端目錄
local_path='/var/www/html/' #本機目錄
local_filename1 = "image-001.jpg" #本機上傳檔名
local_filename2 = "image-002.jpg" #本機上傳檔名
local_filename3 = "image-003.jpg" #本機上傳檔名
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
			
			command='STOR '+local_filename2
			filehankler=open(local_path+local_filename2, 'rb')
			ftp.storbinary(command, filehankler, bufsize) #上傳
			print('本機:'+local_path+local_filename2+' 上傳成功')
			
			command='STOR '+local_filename3
			filehankler=open(local_path+local_filename3, 'rb')
			ftp.storbinary(command, filehankler, bufsize) #上傳
			print('本機:'+local_path+local_filename3+' 上傳成功')
			
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









