import cv2
img = cv2.imread('shape.jpg')
img2 = img.copy()
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(img,150,200)
contours , hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)

for cnt in contours:
    cv2.drawContours(img2,cnt,-1,(255,0,0),4) #畫布 化的東西 -1代表全畫 顏色 線的粗度
    area = cv2.contourArea(cnt)
    if area >500: 
        #print(cv2.arcLength(cnt,True))#(target , 是否閉合)   
        peri = cv2.arcLength(cnt,True)
        vertices = cv2.approxPolyDP(cnt,peri*0.02,True)
        corners = len(vertices)
        x, y, w, h = cv2.boundingRect(vertices)
        cv2.rectangle(img2,(x,y),(x+w,y+h),(0,255,0),4)
        if corners == 3:
            cv2.putText(img2,'triangle',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),4)
        if corners == 4:
            cv2.putText(img2,'rectangle',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),4)
        if corners == 5:
            cv2.putText(img2,'pentagon',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),4)
        if corners == 8:
            cv2.putText(img2,'circle',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),4)

cv2.imshow('img', img)
cv2.imshow('canny',canny)
cv2.imshow('img2',img2)
cv2.waitKey(0)