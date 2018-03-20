#!/usr/bin/env python
#coding:UTF-8
#file name : ex-for-1.py
for i in [1,2,3,4,5]: #若為[1,2,3,4,5,6]，結果？
	if i==6:
		print "i=6，break for"
		break #中止for迴圈
	if i==2:
		print "i=2，繼續執行for"
		continue #略過下行，繼續執行for
	print(i)
#for,else要緊接著，中間不可有程式
else :  #for迴圈若未break，則執行以下
	print "for迴圈若未break，則執行"

print "--end--"

for i in range (11,1,-2):
	print i