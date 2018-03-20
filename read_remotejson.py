#!/usr/bin/env python
#-*- coding:UTF-8 -*-
#file name read_remotejson.py
import time
import json
import ftplib
import socket 
import urllib2
import os
time.sleep(120)
#---FTP---
Host='219.87.162.228' #遠端主機位址
login_account='chander' #登入帳號
login_password='aidsabcgod' #登入密碼
host_path='/chander-pic/' #遠端目錄
local_path='/home/pi/code/' #本機目錄
local_filename1 = 'data.json' #本機上傳檔名
filepath1=local_path + local_filename1
bufsize=1024 #設定緩衝區大小

def upload_json():
	try:
		ftp = ftplib.FTP(Host)
		try:
			ftp.login(login_account, login_password)
			print (ftp.getwelcome()) #登入訊息
			try:
				ftp.cwd(host_path+"pidata/") #切換遠端目錄
				print ('遠端:'+ftp.pwd())
				command='STOR '+local_filename1
				filehankler=open(filepath1, 'rb')
				ftp.storbinary(command, filehankler, bufsize) #上傳
				print('本機:'+filepath1+' 上傳成功')
				
				ftp.quit()
				
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

while True:
	try:
		#======g33 io=========
		#---Json--
		#讀取本機data.json
		# with open('data.json', 'r') as f:
			# data = json.load(f)

		#讀取遠端data.json,http://219.87.162.228/chander/jpg/pidata/data.json
		response = urllib2.urlopen('http://219.87.162.228/chander/jpg/pidata/data.json',timeout=10)
		values = response.read()
		data = json.loads(values)

		io_status = data['g33_io']
		print "g33io= %d" % io_status
		if io_status == 1: #判斷是否為1=啟動
			data.update({ 'g33_io' : 0}) #0為靜止狀態
			#寫入檔案data.json
			with open('data.json', 'w') as f:
				json.dump(data, f)
			
			upload_json()#上傳data.json
			#執行開關
			os.system("sudo python /home/pi/code/g33_on.py")
			
		if io_status == 3: #判斷是否為3=關閉
			data.update({ 'g33_io' : 0})
			#寫入檔案data.json
			with open('data.json', 'w') as f:
				json.dump(data, f)
			
			upload_json()#上傳data.json
			#執行開關
			os.system("sudo python /home/pi/code/g33_off.py")

		#======g35 io=========
		#讀取遠端data.json,http://219.87.162.228/chander/jpg/pidata/data.json
		response = urllib2.urlopen('http://219.87.162.228/chander/jpg/pidata/data.json',timeout=10)
		values = response.read()
		data = json.loads(values)

		io_status = data['g35_io']
		print "g35io= %d" % io_status
		if io_status == 1:
			
			data.update({ 'g35_io' : 0})
			#寫入檔案data.json
			with open('data.json', 'w') as f:
				json.dump(data, f)
			
			upload_json()
			os.system("sudo python /home/pi/code/g35_on.py")
		
		if io_status == 3: #判斷是否為3=關閉
			data.update({ 'g35_io' : 0})
			#寫入檔案data.json
			with open('data.json', 'w') as f:
				json.dump(data, f)
			
			upload_json()#上傳data.json
			#執行開關
			os.system("sudo python /home/pi/code/g35_off.py")

		#======g37 io=========
		#讀取遠端data.json,http://219.87.162.228/chander/jpg/pidata/data.json
		response = urllib2.urlopen('http://219.87.162.228/chander/jpg/pidata/data.json',timeout=10)
		values = response.read()
		data = json.loads(values)

		io_status = data['g37_io']
		print "g37io= %d" % io_status
		if io_status == 1:
			
			data.update({ 'g37_io' : 0})
			#寫入檔案data.json
			with open('data.json', 'w') as f:
				json.dump(data, f)
			
			upload_json()
			os.system("sudo python /home/pi/code/g37_on.py")
			
		if io_status == 3: #判斷是否為3=關閉
			data.update({ 'g37_io' : 0})
			#寫入檔案data.json
			with open('data.json', 'w') as f:
				json.dump(data, f)
			
			upload_json()#上傳data.json
			#執行開關
			os.system("sudo python /home/pi/code/g37_off.py")
			
	except urllib2.HTTPError as e:
		print e.code
		#print ("reboot"),不要reboot ,會一開機就reboot
		
	except urllib2.URLError as e:
		print e.reason
		print ("reboot")
		
	except KeyboardInterrupt:
		print ("KeyboardInterrupt")
		break
