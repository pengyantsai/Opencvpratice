import cv2
from cv2 import erode 
import numpy as np
import random



#img = np.empty((300,300,3),np.uint8 )#300 * 300 ，3 = rgb 
kernel = np.ones((3,3), np.uint8)
img = cv2.imread('colorcolor.jpg')
img = cv2.resize(img,(0,0),fx = 0.5,fy = 0.5)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(img,(5,5),0)
canny = cv2.Canny(img,100,150)
dilate = cv2.dilate(canny,kernel,iterations=1)
erode = cv2.erode(dilate,kernel,iterations=1)

cv2.imshow('gray',gray)
cv2.imshow('img', img)
cv2.imshow('blur', blur)
cv2.imshow('canny', canny)
cv2.imshow('dilate', dilate)
cv2.imshow('erode',erode)
cv2.waitKey(0)





"""
for row in range(300):
    for col in range(img.shape[1]):
        img[row][col] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

cv2.imshow('img', img)
cv2.waitKey(0)


#img[row,col] sloce img
new_img = img[:150,:200]
cv2.imshow('new_img', new_img)


#讀取照片
img = cv2.imread('colorcolor.jpg')
#print(img.shape)
#img = cv2.resize(img,(0,0),fx = 0.5,fy = 0.5)
#cv2.imshow('img',img)


讀取影片   
cap = cv2.VideoCapture('thumb.mp4')
讀取筆電鏡頭
cap = cv2.VideoCapture(0) 
while True:
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame,(0,0),fx = 0.5,fy = 0.5)
        cv2.imshow('video',frame)
    else:
        break
    if cv2.waitKey(10) == ord('q'):
        break
"""