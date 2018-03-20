#!/usr/bin/env python
#-*- coding:UTF-8 -*-
#file name: sht_3_DB.py
#2016-09-02 加入可存入遠端server DB

from sht1x.Sht1x import Sht1x as SHT1x
import mysql.connector
import time
from datetime import datetime
import urllib2

dataPin=11
clkPin=7
sht1x=SHT1x(dataPin,clkPin, SHT1x.GPIO_BOARD)
t1=sht1x.read_temperature_C()
h1=sht1x.read_humidity()
h1=float("{0:.2f}".format(h1))
d1=sht1x.calculate_dew_point(t1,h1)
print ("1->")
print("Temperature:{} Humidity:{} Dew Point:{}".format(t1,h1,d1))

dataPin = 13
clkPin = 15
sht1x = SHT1x(dataPin, clkPin, SHT1x.GPIO_BOARD)
t2=sht1x.read_temperature_C()
h2=sht1x.read_humidity()
h2=float("{0:.2f}".format(h2))
d2=sht1x.calculate_dew_point(t1,h1)
print ("2->")
print("Temperature:{} Humidity:{} Dew Point:{}".format(t2,h2,d2))

dataPin = 29
clkPin = 31
sht1x = SHT1x(dataPin, clkPin, SHT1x.GPIO_BOARD)
t3=sht1x.read_temperature_C()
h3=sht1x.read_humidity()
h3=float("{0:.2f}".format(h3))
d3=sht1x.calculate_dew_point(t1,h1)
print ("3->")
print("Temperature:{} Humidity:{} Dew Point:{}".format(t3,h3,d3))

      
db=mysql.connector.connect(host="localhost",user="root",passwd="aidsabcgod",db="test")
curs=db.cursor()
#db.close()
try:
        now=time.time()
        now2=datetime.now()
        #[ temp,hum ] = dht(dht_sensor_port,dht_sensor_type)		#Get the temperature and Humidity from the DHT sensor
        #print time.ctime(now)," temp =", temp, "C\thumidity =", hum,"%" 	
        #print now2," temp =", temp, "C\thumidity =", hum,"%" 
        dbt1 = str(t1)
        dbh1 = str(h1)
        dbt2 = str(t2)
        dbh2 = str(h2)
        dbt3 = str(t3)
        dbh3 = str(h3)
        dbt4=0
        dbh4=0
        
        #setRGB(0,128,64)
        #setRGB(0,255,0)
        #setText("Temp:" + t + "C      " + "Humidity :" + h + "%")

        dht_insert="insert into temp2(date, ymd, hms, t1, h1, t2, h2, t3, h3, t4, h4) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        #dhtrecord=(time.ctime(now),t,h)
        now3=str(now2.year) + "-" + str(now2.month)+"-"+str(now2.day)+" "+str(now2.hour)+":"+str(now2.minute)+":"+str(now2.second)
        
        now_ymd=str(now2.year) + "-" + str(now2.month)+"-"+str(now2.day)       
        now_hms=str(now2.hour) + ":" + str(now2.minute)+":"+str(now2.second) 

        dhtrecord=(now3,now_ymd,now_hms,dbt1,dbh1,dbt2,dbh2,dbt3,dbh3,dbt4,dbh4)
        curs.execute(dht_insert, dhtrecord)
        db.commit()
        
except (IOError,TypeError) as e:
        print "Error"
        #curs.close()
        #db.close()
except KeyboardInterrupt:
        print "KeyboardInterrupt"
        curs.close()
        db.close()

#存入遠端server
now3=str(now2.year) + "-" + str(now2.month)+"-"+str(now2.day)+"%20"+str(now2.hour)+":"+str(now2.minute)+":"+str(now2.second)

#url="http://192.168.60.107/"
url="http://219.87.162.228/chander/"

page1="insertdb.aspx?"
date="date="+str(now3)
ymd="ymd="+str(now_ymd)
hms="hms="+str(now_hms)
mt1="t1="+dbt1
mh1="h1="+dbh1
mt2="t2="+dbt2
mh2="h2="+dbh2
mt3="t3="+dbt3
mh3="h3="+dbh3
mt4="t4="+str(dbt4)
mh4="h4="+str(dbh4)
print (url+page1+date+"&"+ymd+"&"+hms+"&"+mt1+"&"+mh1+"&"+mt2+"&"+mh2+"&"+mt3+"&"+mh3+"&"+mt4+"&"+mh4)
request=urllib2.Request(url+page1+date+"&"+ymd+"&"+hms+"&"+mt1+"&"+mh1+"&"+mt2+"&"+mh2+"&"+mt3+"&"+mh3+"&"+mt4+"&"+mh4)

try:
	response=urllib2.urlopen(request,timeout=10)
	print response.read()


except urllib2.HTTPError as e:
	print e.code
except urllib2.URLError as e:
	print e.reason