#!/usr/bin/env python
#-*- coding:UTF-8 -*-
#file name: count_file.py
import os

max_files=500 #當檔案數大於一定值

count_y=0 #改檔名用

#時排排序,
# def sorted_ls(path):
	# mtime = lambda f: os.stat(os.path.join(path, f)).st_mtime
	# return list(sorted(os.listdir(path), key=mtime))

dir="/var/www/html/image/image1/"
print dir
#list = os.listdir(dir) # 獲得目錄內容

# 獲得時間排序後的目錄內容
mtime = lambda f: os.stat(os.path.join(dir, f)).st_mtime
list=sorted(os.listdir(dir), key=mtime)

number_files = len(list)
print (str(number_files)+"\n")
#print (str(list)+"\n")
# print (str(list[0])+"\n")
# print (str(list[1])+"\n")
# print (str(list[2])+"\n")

while number_files > max_files : #當檔案數大於一定值
	for x in list :
		print x #印出單一檔名
		os.system("rm -rf "+ dir + x) #刪檔
		list = os.listdir(dir) # 獲得目錄內容
		number_files = len(list)
		if number_files == max_files : #保留總檔案數,數量
			print ("break")
			break #exit for
			break #exit while


print (str(number_files)+"\n")

#批次更改檔名
# for x in list :
	# print x #印出單一檔名
	# os.system("mv " + dir + x + " " + dir + "image1-{0:03d}.jpg".format(count_y))
	# count_y = count_y + 1

dir="/var/www/html/image/image2/"
print dir
#list = os.listdir(dir) # 獲得目錄內容

# 獲得時間排序後的目錄內容
mtime = lambda f: os.stat(os.path.join(dir, f)).st_mtime
list=sorted(os.listdir(dir), key=mtime)

number_files = len(list)
print (str(number_files)+"\n")
#print (str(list)+"\n")

while number_files > max_files : #當檔案數大於一定值
	for x in list :
		print x #印出單一檔名
		os.system("rm -rf "+ dir + x) #刪檔
		list = os.listdir(dir) # 獲得目錄內容
		number_files = len(list)
		if number_files == max_files : #保留總檔案數,數量
			print ("break")
			break #exit for
			break #exit while

print (str(number_files)+"\n")

dir="/var/www/html/image/image3/"
print dir
#list = os.listdir(dir) # 獲得目錄內容
# 獲得時間排序後的目錄內容
mtime = lambda f: os.stat(os.path.join(dir, f)).st_mtime
list=sorted(os.listdir(dir), key=mtime)
number_files = len(list)
print (str(number_files)+"\n")
#print (str(list)+"\n")
# print (str(list[0])+"\n")
# print (str(list[1])+"\n")
# print (str(list[2])+"\n")

while number_files > max_files : #當檔案數大於一定值
	for x in list :
		print x #印出單一檔名
		os.system("rm -rf "+ dir + x) #刪檔
		list = os.listdir(dir) # 獲得目錄內容
		number_files = len(list)
		if number_files == max_files : #保留總檔案數,數量
			print ("break")
			break #exit for
			break #exit while
			
print (str(number_files)+"\n")
