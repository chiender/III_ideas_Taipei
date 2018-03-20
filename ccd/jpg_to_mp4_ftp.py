#!/usr/bin/env python
#-*- coding:UTF-8 -*-
#file name: jpg_to_mp4_ftp.py
#將jpg轉成動畫mp4,並上傳至ftp
import ftplib
import socket 
from os import system
import time
from datetime import datetime


#將image1-xxx.jpg 轉成 image1.mp4
system("sudo ffmpeg -framerate 10 -pattern_type glob -i '/var/www/html/image/image1/*.jpg' -c:v libx264 -vf fps=30 -pix_fmt yuv420p -y /var/www/html/image/image1.mp4")
print ("image1.mp4->OK!")

#將image2-xxx.jpg 轉成 image2.mp4
#system('ffmpeg -framerate 2 -start_number 0 -i /var/www/html/image/image2/* -c:v libx264 -vf fps=30 -pix_fmt yuv420p -y /var/www/html/image/image2.mp4')
system("sudo ffmpeg -framerate 10 -pattern_type glob -i '/var/www/html/image/image2/*.jpg' -c:v libx264 -vf fps=30 -pix_fmt yuv420p -y /var/www/html/image/image2.mp4")
print ("image2.mp4->OK!")

#將image3-xxx.jpg 轉成 image3.mp4
#system('ffmpeg -framerate 2 -start_number 0 -i /var/www/html/image/image3/* -c:v libx264 -vf fps=30 -pix_fmt yuv420p -y /var/www/html/image/image3.mp4')
system("sudo ffmpeg -framerate 10 -pattern_type glob -i '/var/www/html/image/image3/*.jpg' -c:v libx264 -vf fps=30 -pix_fmt yuv420p -y /var/www/html/image/image3.mp4")
print ("image3.mp4->OK!")

Host='219.87.162.228' #遠端主機位址
login_account='chander' #登入帳號
login_password='aidsabcgod' #登入密碼
host_path='/chander-pic/image' #遠端目錄
local_path='/var/www/html/image/' #本機目錄
local_filename1 = "image1.mp4" #本機上傳檔名
local_filename2 = "image2.mp4" #本機上傳檔名
local_filename3 = "image3.mp4" #本機上傳檔名
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

