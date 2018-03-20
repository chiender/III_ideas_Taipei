#!/usr/bin/env python
#-*- coding:UTF-8 -*-
#file name g33_on.py
#打開pin 35，20秒，計算流量，存入data.json，上傳至server.2017/03/01
import RPi.GPIO as GPIO
import time
import json
import ftplib
import socket 
import urllib2

#{'g33_now':10,'g33_all':100,'g35_now':10,'g35_all':100,'g37_now':10,'g37_all':100,'vol':7,'cur':1.2,}

#--read water class--
import flow_meter_class as flow
water_sensor=40
#--read water class--
led=35
#寫入data.json的key
meter_all='g35_all'
meter_now='g35_now'


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.OUT)

try:
	#--water_meter--
	x=0
	total_flow=0
	flow_meter=flow.flow(water_sensor)
	#--water_meter--
	#on=false
	GPIO.output(led,False)
	print "菜圃（二），澆水－開。20秒後會自動關閉澆水，並重新載入原首頁。"
	
	#--water_meter,累積10秒流水量.--
	while x < 10:
		water=flow_meter.read_flow()
		print "Entering Water: %.3f Liters" % (water)
		#計算總流量
		total_flow = total_flow + water
		x +=1
	
	total_flow=float("{0:.3f}".format(total_flow))
	print "\ntotal Water: %.3f Liters" % total_flow
	#--water_meter--
	
	#time.sleep(20) off=true
	GPIO.output(led,True)
	
	

except KeyboardInterrupt:
	print ("KeyboardInterrupt")
	GPIO.cleanup()


#---FTP---
Host='219.87.162.228' #遠端主機位址
login_account='chander' #登入帳號
login_password='aidsabcgod' #登入密碼
host_path='/chander-pic/' #遠端目錄
local_path='/home/pi/code/' #本機目錄
local_filename1 = 'data.json' #本機上傳檔名
filepath1=local_path + local_filename1
bufsize=1024 #設定緩衝區大小


#---Json--
#讀取本機data.json
# with open('data.json', 'r') as f:
	# data = json.load(f)

#讀取遠端data.json,http://219.87.162.228/chander/jpg/pidata/data.json
response = urllib2.urlopen('http://219.87.162.228/chander/jpg/pidata/data.json')
values = response.read()
data = json.loads(values)

print data[meter_all]

#加之前的流量=所有流量
all_flow=data[ meter_all ] + total_flow
#更新最近流量
data.update({ meter_now : total_flow})
#更新所有流量
data.update({ meter_all : all_flow}) 

#寫入檔案data.json
with open('data.json', 'w') as f:
	json.dump(data, f)
	
print data[ meter_all ]
#---Json--


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

exit()


