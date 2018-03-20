#!/usr/bin/env python
#-*- coding:UTF-8 -*-
#file name : file_rw.py

#若沒有建檔,會自動建檔,寫入檔案
file = open('1.txt','w')
file.write('python\n')
file.writelines("test1\n")
file.writelines("test2\n")
file.close()

#讀取檔案
file=open('1.txt','r')
s=file.read() #讀取檔案全部內容
print (s)

# #讀取檔案
# file=open('1.txt','r')
# s=file.readline() #讀取檔案第一行內容
# print (s)

# #讀取檔案
# file=open('1.txt','r')
# s=file.read(5) #讀取第一行,前5個字元,pytho
# print (s)

# #讀取檔案
# file=open('1.txt','r')
# #將檔案每一行,讀取到串列中
# s=file.readlines() 
# print (s) #['python\n', 'test1\n', 'test2\n']
# print (s[1]) #test1

# with open('1.txt', 'wb') as file:
	# file.seek(3)
	# file.write("test3")
# file.closed


#讀取檔案至data串列
# with open('1.txt','r') as f:
	# data = f.readlines()
	
# for line in data:
	# #分割字串
	# words = line.split()
	# print words


