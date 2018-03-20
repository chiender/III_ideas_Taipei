#!/usr/bin/env python
#-*- coding:UTF-8 -*-
#file name: sht_3_DB.py
import time
from datetime import datetime

now2=datetime.now()
now3="image1-%d%02d%02d%02d.jpg" % (now2.year,now2.month,now2.day,now2.hour)

print (str(now2)+"\n")
print (str(now3)+"\n")