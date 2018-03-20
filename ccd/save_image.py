#!/usr/bin/env python
#-*- coding:UTF-8 -*-
#file name:save_image.py
import cv2

#0-> /dev/video0 :也可以是filename
cap=cv2.VideoCapture(0)

#gain=10
#cap.set(cv2.cv.CV_CAP_PROP_GAIN,gain)

#exposure=3
#cap.set(cv2.cv.CV_CAP_PROP_EXPOSURE,exposure)

#brightness=-1	#在某些ccd可以
#cap.set(cv2.cv.CV_CAP_PROP_BRIGHTNESS,brightness)

#contrast=10	#在某些ccd可以
#cap.set(cv2.cv.CV_CAP_PROP_CONTRAST,contrast)

#saturation=20
#cap.set(cv2.cv.CV_CAP_PROP_SATURATION,saturation)


ret,img=cap.read() #640x480
#視窗呈現
cv2.imshow('image_save',img)
cv2.imwrite('image-2.jpg',img)
#按任意鍵關閉視窗
cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release()
exit()


