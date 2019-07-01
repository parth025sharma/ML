#!/usr/bin/python3
import cv2
#starting cam
cap=cv2.VideoCapture(0) #link of ip webcam to connect "  http://192.168.43.135:8080/video?q=" past in cv2.ViseoCapture()
# camera number ------- video file -----url  can also be given here
# status,frame=cap.read()
#now taking frame/picture  only and saVING IN   tp{1,2,3}
tp1=cap.read()[1]# take1
tp2=cap.read()[1]#take2
tp3=cap.read()[1]#take3 
#to makke more perfact 
gray1=cv2.cvtColor(tp1,cv2.COLOR_BGR2GRAY)# converting into gray
gray2=cv2.cvtColor(tp2,cv2.COLOR_BGR2GRAY)# converting into gray
gray3=cv2.cvtColor(tp3,cv2.COLOR_BGR2GRAY)# converting into gray
#now creating image difff
def img_diff(x,y,z):
    #   diff b/w x,y--gray1 & gray2
    d1=cv2.absdiff(x,y)
    #   diff b/w y,z--gray2 & gray3
    d2=cv2.absdiff(y,z)
    #   absolute diff d1-d2
    finalimg=cv2.bitwise_and(d1,d2)
    return finalimg
    # there are two ways to get diff 1- by Numpy 2- by cv
    # 2- absdiff in cv2


# now apllying function
while cap.isOpened():
    status,frame=cap.read() #   continue image taker
    motionimg=img_diff(gray1,gray2,gray3)
    # replacing image frame as to make it continos
    gray1=gray2
    gray2=gray3
    gray3=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # taking live image to gray 3 and updating gray3 with live image or live new image
    # LIve img
    cv2.imshow('live',frame)
    #   motion image 
    cv2.imshow('motion',motionimg)  #  motion detect
    if cv2.waitKey(10) & 0xff == ord("q"):
        break
cv2.destroyAllWindows()
cap.release()
