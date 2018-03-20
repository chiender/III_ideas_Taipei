#!/usr/bin/python
#-*- coding:UTF-8 -*-
#file name: find_usb.py
import sys
import usb.core

#找尋所有USB
dev = usb.core.find(find_all=True)
# 列出所有USB PID VID 及 decimal and hex
for cfg in dev:
  sys.stdout.write('Decimal VendorID=' + str(cfg.idVendor) + ' & ProductID=' + str(cfg.idProduct) + '\n')
  sys.stdout.write('Hexadecimal VendorID=' + hex(cfg.idVendor) + ' & ProductID=' + hex(cfg.idProduct) + '\n\n')
  
