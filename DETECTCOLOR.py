import cv2
import numpy as np
def empty(v):
    pass

img = cv2.imread('XiWinnie.jpg')
img = cv2.resize(img,(0,0),fx = 0.5,fy = 0.5)

cv2.namedWindow('tracebar')
cv2.resizeWindow('tracebar' , 640,320)

cv2.createTrackbar('HUE MIN','tracebar', 0 , 179 ,empty )#hue frome 1 to 179
cv2.createTrackbar('HUE MAX','tracebar', 179 , 179 ,empty )
cv2.createTrackbar('SAT MIN','tracebar', 0 , 255 ,empty )
cv2.createTrackbar('SAT MAX','tracebar', 255 , 255 ,empty )
cv2.createTrackbar('VALUE MIN','tracebar', 0 , 255 ,empty )
cv2.createTrackbar('VALUE MAX','tracebar', 255 , 255 ,empty )
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV) # HUE = 色調 ,STURATION = 飽和度 , VALUE = 亮度 
#HSV 更容易過濾顏色

while True:
    h_min = cv2.getTrackbarPos('HUE MIN','tracebar')
    h_max = cv2.getTrackbarPos('HUE MAX','tracebar')
    s_min = cv2.getTrackbarPos('SAT MIN','tracebar')
    s_max = cv2.getTrackbarPos('SAT MAX','tracebar')
    v_min = cv2.getTrackbarPos('VALUE MIN','tracebar')
    v_max = cv2.getTrackbarPos('VALUE MAX','tracebar')
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max]) 
    mask = cv2.inRange(hsv,lower,upper)
    result = cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow('hsv', hsv)
    cv2.imshow('img', img)
    cv2.imshow('mask',mask)
    cv2.imshow('result', result)
    cv2.waitKey(1)
 






