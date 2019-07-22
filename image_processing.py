# -*- coding: utf-8 -*-

#Created on Sun Oct  7 11:10:36 2018
#0
#@author: Sharif
# ***read README file****

import cv2
import numpy as np
from PIL import Image
import imutils
import urllib.request as ur

# Connect phone and laptop in same hotspot 
# Use the following ur.urlretrieve("http://xxx.xx.xx.xx:xxxx/captured_image_address","default") step 5 
# remove hash_tag befor ur.urlretrieve to get image from wifi file transfer
# crop the image manually in phone before compiling
 
ur.urlretrieve("http://172.20.10.14:1234/storage/emulated/0/1.jpg","up.jpg")
ur.urlretrieve("http://172.20.10.14:1234/storage/emulated/0/2.jpg","face.jpg")
ur.urlretrieve("http://172.20.10.14:1234/storage/emulated/0/3.jpg","right.jpg")
ur.urlretrieve("http://172.20.10.14:1234/storage/emulated/0/4.jpg","bottom.jpg")
ur.urlretrieve("http://172.20.10.14:1234/storage/emulated/0/5.jpg","left.jpg")
ur.urlretrieve("http://172.20.10.14:1234/storage/emulated/0/6.jpg","down.jpg")

# If input image is stored manually to the program folder ,name the captured image as the file nae in address dictionary //up.jpg, face.jpg,,,,down.jpg
# Step 5: image from phone, will be detected automatically by the program

address={"up.jpg":'up',
         "face.jpg":'face',
         "right.jpg":'right',
         "bottom.jpg":'bottom',
         "left.jpg":'left',
         "down.jpg":'down'
         }

#To detect cube and crop the image automatically , better crop it manually in phone before compiling the program
#//////////////////////////////////////////////////////////////////////////////
#for X,Y in address.items():
#    image = cv2.imread(X)
#    img = cv2.blur(image,(5,5))
#    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#    gray = cv2.bilateralFilter(gray, 11, 17, 17)
#    edged = cv2.Canny(gray, 150, 200)
#    contour = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#    contour = imutils.grab_contours(contour)
#    contour = sorted(contour, key = cv2.contourArea, reverse = True)[:10]
#    screenCnt = None
#    for cnt in contour:
#        peri = cv2.arcLength(cnt, True)
#        approx = cv2.approxPolyDP(cnt, 0.015 * peri, True)
#        if len(approx) == 4:
#            Cnt = approx
#            x,y,w,h = cv2.boundingRect(Cnt)
#            break
#        
#        print(x,y,w,h)
#        i=image[y:y+h, x:x+w]
#        cv2.drawContours(image, [Cnt], -1, (0, 255, 0), 3)
#        cv2.imshow("Cropped", i)
#        cv2.imwrite(X, i)
#        cv2.waitKey(0)
#        cv2.destroyAllWindows()
#//////////////////////////////////////////////////////////////////////////////

hsvcolor = {
            'red':([0, 80,80], [10, 255, 255]),     
            'orange':([10,80, 80], [20, 255, 255]),        
            #'white':([0, 0, 0], [0, 80, 255]),
            'green':([33,80,40], [100,255,255]),
            'yellow':([20, 100, 100], [30, 255, 255]),
            'blue':([100, 50, 50], [130, 255, 255])
            }


for X,Y in address.items():

    img=cv2.imread(X)
    img=cv2.resize(img,(500,500))
    cv2.imshow(Y,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
 
       
    for color,(lower, upper) in hsvcolor.items():
        lower = np.array(lower, dtype = "uint8")
        upper = np.array(upper, dtype = "uint8")
        mask=cv2.inRange(hsv,lower,upper)
        cv2.imwrite(Y+'_'+color+'.jpg',mask)
        cv2.imshow(Y+'_'+color,mask)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    