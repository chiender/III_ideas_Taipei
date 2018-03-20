#!/usr/bin/env python
#-*- coding:UTF-8 -*-
#file name:read_volandcur.py
#同時讀取電壓，電流
#board pins；pin 3=SDA；pin 5=SCL
import time
from smbus import SMBus
import json
import ftplib
import socket 
import urllib2

pcf_address = 0x48

AIN0=0 #讀入電壓腳位
AIN1=1 #讀入電流腳位,原本potentiometer
AIN2=2 #thermistor
AIN3=3 #light dependent resistor
read_pin=AIN0

bus = SMBus(1)
# i2cset -y 1 0x49 0x01
bus.write_byte(pcf_address,read_pin)

#---讀取電壓---
try:
	x=0
	total_vol=0
	reading=0
	reading = bus.read_byte(pcf_address) # read A/D i2cget -y 1 0x49
	while x < 4 :
		time.sleep(1)#sec
		reading = bus.read_byte(pcf_address) # read A/D i2cget -y 1 0x49
		#轉換成電壓,最高電壓為4.44v,並非5V,256為8bit A/D
		vout=(float(reading)*5.07)/256
		vin=float(vout) / 0.2 #透過Arduino 25V Voltage Sensor Module,計算輸入
		print('Analog '+ str(read_pin)+' reading: '+str(reading))
		print "0~5V= %.3f v" % vout #0~5V電壓顯示
		print "0~25V= %.3f v" % vin #0~25V輸入電壓顯示
		x += 1
		total_vol = total_vol + vin

	avg_vol = total_vol / 4
	if avg_vol < 0.05 :
		avg_vol = 0
	
	avg_vol=float("{0:.2f}".format(avg_vol))
	print "平均電壓"
	print avg_vol

except KeyboardInterrupt:
	print ("KeyboardInterrupt")

#---讀取電流---
read_pin=AIN1
bus = SMBus(1)
# i2cset -y 1 0x49 0x01
bus.write_byte(pcf_address,read_pin)

try:
	x=0
	total_cure=0
	reading=0
	reading = bus.read_byte(pcf_address) # read A/D i2cget -y 1 0x49
	while x < 4 :
		time.sleep(1)#sec
		reading = bus.read_byte(pcf_address) # read A/D i2cget -y 1 0x49
		#轉換成電壓,最高電壓為4.44v,並非5V,256為8bit A/D
		vout=(float(reading)*5.07)/256
		print('Analog '+ str(read_pin)+' reading: '+str(reading))
		#電流計算A＝（V讀入電壓－2.5V）/0.185V,-2.23
		cure=(float(vout)-2.53)/0.185
		print "Current= %.3f A" % cure
		total_cure = cure + total_cure
		x +=1
	
	avg_cure = total_cure / 4
	if avg_cure < 0.05 :
		avg_cure = 0
	
	avg_cure=float("{0:.2f}".format(avg_cure))
	print "平均電流"
	print avg_cure
	
except KeyboardInterrupt:
	print ("KeyboardInterrupt")

	
#---Json--
#讀取本機data.json
# with open('data.json', 'r') as f:
	# data = json.load(f)

#讀取遠端data.json,http://219.87.162.228/chander/jpg/pidata/data.json
response = urllib2.urlopen('http://219.87.162.228/chander/jpg/pidata/data.json')
values = response.read()
data = json.loads(values)

print "遠端讀取資料"
print data['vol']
print data['cur']

#更新電壓
data.update({ 'vol' : avg_vol})
#更新電流
data.update({ 'cur' : avg_cure}) 

#寫入檔案data.json
with open('data.json', 'w') as f:
	json.dump(data, f)

print "寫入資料"
print data['vol']
print data['cur']
#---Json--


#---FTP---
Host='219.87.162.228' #遠端主機位址
login_account='chander' #登入帳號
login_password='aidsabcgod' #登入密碼
host_path='/chander-pic/' #遠端目錄
local_path='/home/pi/code/' #本機目錄
local_filename1 = 'data.json' #本機上傳檔名
filepath1=local_path + local_filename1
bufsize=1024 #設定緩衝區大小

#--FTP--
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