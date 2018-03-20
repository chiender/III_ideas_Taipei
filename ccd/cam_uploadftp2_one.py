#!/usr/bin/env python
#-*- coding:UTF-8 -*-
#file name:cam_uploadftp2.py
#以時間存成檔名,並保留每一張照片,不覆蓋,並上傳至後台.

import ftplib
import socket 
from SimpleCV import Camera,Image,Color
#from os import system
import os
import time
from datetime import datetime
import cv2

print ("try...")

now2=datetime.now() #顯示現在時間
#時間組合2017011214,年月日時
#now3="%d%02d%02d%02d" % (now2.year,now2.month,now2.day,now2.hour)

#檔名-時間組合2017011214,年月日時,分
now3="%d%02d%02d%02d%02d" % (now2.year,now2.month,now2.day,now2.hour,now2.minute)

try :
	#相機1
	#0-> /dev/video0 :也可以是filename
	#cap=cv2.VideoCapture(0)
	
	cam=Camera(0,{"width":800,"height":600})	#320X240
	img1=cam.getImage()
	time.sleep(3)
	now2=str(datetime.now()) #顯示現在時間,照片tag
	img1=cam.getImage()
	filename1="image1-"+ now3 + ".jpg" #檔名
	#image1-2017011214.jpg,在寫在/var/www/html/image/image1下才能存檔
	filepath1="/var/www/html/image/image1/" + filename1
	#img1.drawText(now2,30,220,Color.RED,30)
	img1.drawText(now2,200,550,Color.RED,40)
	# img1.save(filepath1)
	# print ("SAVE:" + filename1)
	
	# #相機2
	# cam=Camera(1,{"width":320,"height":240})	#320X240
	# img2=cam.getImage()
	# time.sleep(3)
	# now2=str(datetime.now()) #顯示現在時間,照片tag
	# img2=cam.getImage()
	# filename2="image2-"+ now3 + ".jpg" #檔名
	# #image1-2017011214.jpg,在寫在/var/www/html/image/image2下才能存檔
	# filepath2="/var/www/html/image/image2/" + filename2
	# img2.drawText(now2,30,220,Color.RED,30)
	# # img2.save(filepath2)
	# # print ("SAVE:" + filename2)

	# #相機3
	# cam=Camera(2,{"width":320,"height":240})	#320X240
	# img3=cam.getImage()
	# time.sleep(3)
	# now2=str(datetime.now()) #顯示現在時間,照片tag
	# img3=cam.getImage()
	# filename3="image3-"+ now3 + ".jpg" #檔名
	# #image1-2017011214.jpg,在寫在/var/www/html/image/image3下才能存檔
	# filepath3="/var/www/html/image/image3/" + filename3
	# img3.drawText(now2,30,220,Color.RED,30)
	
	img1.save(filepath1)
	print ("SAVE:" + filename1)
	# img2.save(filepath2)
	# print ("SAVE:" + filename2)
	# img3.save(filepath3)
	# print ("SAVE:" + filename3)
	exit()
	
except (IOError,TypeError, AttributeError) as e:
	print ("camera error")
	#像機使用一陣子會出現libv4l2: error setting pixformat: Device or resource busy
	#在AttributeError
	#砍掉python的工作行程即可回復
	#os.system("killall -9 python")
	#print ("killall python")
	
	print ("reboot")
	#os.system("sudo reboot")
	exit()

# Host='219.87.162.228' #遠端主機位址
# login_account='chander' #登入帳號
# login_password='aidsabcgod' #登入密碼
# host_path='/chander-pic/image/' #遠端目錄
# local_path='/var/www/html/image/' #本機目錄
# local_filename1 = filename1 #本機上傳檔名
# # local_filename2 = filename2 #本機上傳檔名
# # local_filename3 = filename3 #本機上傳檔名
# bufsize=1024 #設定緩衝區大小



# try:
	# ftp = ftplib.FTP(Host)
	# try:
		# ftp.login(login_account, login_password)
		# print (ftp.getwelcome()) #登入訊息
		# try:
			# ftp.cwd(host_path+"image1/") #切換遠端目錄
			# print ('遠端:'+ftp.pwd())
			# command='STOR '+local_filename1
			# filehankler=open(filepath1, 'rb')
			# ftp.storbinary(command, filehankler, bufsize) #上傳
			# print('本機:'+filepath1+' 上傳成功')
			
			# # ftp.cwd(host_path+"image2/") #切換遠端目錄
			# # command='STOR '+local_filename2
			# # filehankler=open(filepath2, 'rb')
			# # ftp.storbinary(command, filehankler, bufsize) #上傳
			# # print('本機:'+filepath2+' 上傳成功')
			
			# # ftp.cwd(host_path+"image3/") #切換遠端目錄
			# # command='STOR '+local_filename3
			# # filehankler=open(filepath3, 'rb')
			# # ftp.storbinary(command, filehankler, bufsize) #上傳
			# # print('本機:'+filepath3+' 上傳成功')
			
			# ftp.quit()
			# exit()
		# except (ftplib.error_perm):
			# print 'ERROR:遠端目錄不存在' 
			# ftp.quit()
			# exit()
	# except (ftplib.error_perm):
		# print 'ERROR:無法登入,請檢查帳號或密碼' 
		# ftp.quit()
		# exit()
# except(socket.error, socket.gaierror): 
	# print 'ERROR:無法連線 " %s"' % Host
	# exit()

# exit()








