import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow("Tracking")


cv2.createTrackbar("LH","Tracking",0,255,nothing)
cv2.createTrackbar("LS","Tracking",0,255,nothing)
cv2.createTrackbar("LV","Tracking",0,255,nothing)

cv2.createTrackbar("UH","Tracking",255,255,nothing)
cv2.createTrackbar("US","Tracking",255,255,nothing)
cv2.createTrackbar("UV","Tracking",255,255,nothing)

while True:
    frame=cv2.imread("rajkamalrajkamal.jpg")
    #isTrue,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    
    LH=cv2.getTrackbarPos("LH","Tracking")
    LS=cv2.getTrackbarPos("LS","Tracking")
    LV=cv2.getTrackbarPos("LV","Tracking")
    
    UH=cv2.getTrackbarPos("UH","Tracking")
    US=cv2.getTrackbarPos("US","Tracking")
    UV=cv2.getTrackbarPos("UV","Tracking")
    
    l_b=np.array([LH,LS,LV])
    u_b=np.array([UH,US,UV])
    
    mask=cv2.inRange(hsv,l_b,u_b)
    
    result=cv2.bitwise_and(frame,frame,mask=mask)
    
    cv2.imshow("frame",frame)
    cv2.imshow("hsv",hsv)
    cv2.imshow("mask",mask)
    k=cv2.waitKey(1)&0xff
    if k==27:
        break
cv2.destroyAllWindows()
    