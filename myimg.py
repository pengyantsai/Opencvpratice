import cv2 
import numpy as np

img = np.zeros((600,600,3),np.uint8)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(255,0,0),1) #目標 起點 終點 顏色 線的粗度
cv2.rectangle(img,(0,0),(400,300),(0,255,0),2) #目標 左上點 右下點 顏色 線的粗度 or use cv2.FILLED 填滿
cv2.circle(img,(300,400),30,(0,0,255),3)#目標 圓心 半徑 顏色 線的粗度 or use cv2.FILLED 填滿
cv2.putText(img,'hellow',(100,500),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2) #目標 字串 位置 字體 字體大小 顏色 粗度

cv2.imshow('img', img)
cv2.waitKey(0)




