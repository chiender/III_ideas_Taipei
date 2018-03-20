#!/usr/bin/python
#-*- coding:UTF-8 -*-
#file name: find_usb_device.py
import usb.core

dev = usb.core.find(idVendor=0x46d, idProduct=0xc06c)
if dev is None:
	raise ValueError('Our device is not connected')
else :
	print ('Decimal VendorID=' + str(dev.idVendor) + ' & ProductID=' + str(dev.idProduct) + '\n')
	print ('Hexadecimal VendorID=' + hex(dev.idVendor) + ' & ProductID=' + hex(dev.idProduct) + '\n')
	
	print (str(dev.bNumConfigurations)+'\n')
	print (str(dev.bDeviceClass)+'\n')

#dev.set_configuration()
