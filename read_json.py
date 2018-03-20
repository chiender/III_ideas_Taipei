#!/usr/bin/env python
#-*- coding:UTF-8 -*-
#file name : read_json.py
import json
data = {'g33_now':10,'g33_all':100,'g35_now':10,'g35_all':100,'g37_now':10,'g37_all':100,'vol':7,'cur':1.2,}

#寫入檔案data.json
with open('data.json', 'w') as f:
	json.dump(data, f)

print data
#data.update({'g33_now':20})

# with open('data.json', 'w') as f:
	# json.dump(data, f)
	
#讀取
with open('data.json', 'r') as f:
	data = json.load(f)

print data['g33_now']
	
# data1 =  { 'b' : 789 , 'c' : 456 , 'a' : 123 }
# data2 =  { 'a' : 123 , 'b' : 789 , 'c' : 456 }
# d1 =  json.dumps(data1,sort_keys = True )
# d2 =  json.dumps(data2)
# d3 =  json.dumps(data2,sort_keys = True )
# print  d1
# print  d2
# print  d3
