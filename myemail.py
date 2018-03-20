#!/usr/bin/env python
#-*- coding:UTF-8 -*-
#file name:myemail.py  檔名不能用email.py
import smtplib
from datetime import datetime

host="smtp.live.com" #hotmail smtp server
port="587" #smtp port 587 for ssl
user="chander_service@hotmail.com" #登入帳號
passwd="971206@abcgod" #登入密碼

subject="Python 測試信件" #主旨
fromaddr="chander_service@hotmail.com" #寄件者

#單一收件者
toaddr="chiender@iii.org.tw" 

#多人收件者
#toaddr=["chiender@iii.org.tw", "lin.chander@gmail.com"]
#manytoaddr = ",".join(toaddr)

#內容
text="\
This is a test mail.\n\
這是一封測試信。\n"\
+ str(datetime.now()) 

#單一收件者
msg=("From: %s\nTo: %s\nSubject: %s\n\n"\
% (fromaddr,toaddr,subject))
#多人收件者
"""
msg=("From: %s\nTo: %s\nSubject: %s\n\n"\
% (fromaddr,manytoaddr,subject))
"""
msg=msg+text


try:
	smtp=smtplib.SMTP() 
	smtp.connect(host,port) #連接
	#smtp.set_debuglevel(1) #除錯模式
	smtp.ehlo()
	smtp.starttls() #SSL
	smtp.login(user,passwd) #登入
	smtp.sendmail(fromaddr,toaddr,msg) #寄信
	smtp.quit()
	print ("send successed!")

except Exception as e:
	print ("Sent email error!")

