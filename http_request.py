#!/usr/bin/env python
#-*- coding:UTF-8 -*-
#file name: http_request.py
import urllib2
import datetime

now2=datetime.datetime.now()
now3=str(now2.year) + "-" + str(now2.month)+"-"+str(now2.day)+"%20"+str(now2.hour)+":"+str(now2.minute)+":"+str(now2.second)
now_ymd=str(now2.year) + "-" + str(now2.month)+"-"+str(now2.day)       
now_hms=str(now2.hour) + ":" + str(now2.minute)+":"+str(now2.second) 

url="http://192.168.60.107/"

#page1="default.aspx?"
#date="date="+str(now3)
#temp="temp=34"
#hum="hum=98"
#request=urllib2.Request("http://192.168.60.107/default.aspx?date=2016-09-01%2014:00&temp=34&hum=98")
#request=urllib2.Request(url+page1+date+"&"+temp+"&"+hum)


temp=34
humd=66
page1="insertdb.aspx?"
date="date="+str(now3)
ymd="ymd="+str(now_ymd)
hms="hms="+str(now_hms)
t1="t1="+str(temp)
h1="h1="+str(humd)
t2="t2="+str(temp)
h2="h2="+str(humd)
t3="t3="+str(temp)
h3="h3="+str(humd)
t4="t4="+str(temp)
h4="h4="+str(humd)

#request=urllib2.Request("http://192.168.60.107/default.aspx?date=2016-09-01%2014:00&temp=34&hum=98")
request=urllib2.Request(url+page1+date+"&"+ymd+"&"+hms+"&"+t1+"&"+h1+"&"+t2+"&"+h2+"&"+t3+"&"+h3+"&"+t4+"&"+h4)

try:
	response=urllib2.urlopen(request,timeout=10)
	print response.read()


except urllib2.HTTPError as e:
	print e.code
except urllib2.URLError as e:
	print e.reason

# except urllib2.URLError, e:

	# if hasattr(e, 'reason'):
		# print 'We failed to reach a server.'
		# print 'Reason: ', e.reason

	# elif hasattr(e, 'code'):
		# print 'The server could not fulfill the request.'
		# print 'Error code: ', e.code




