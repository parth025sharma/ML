#!/usr/bin/python3
import cv2
#starting cam
cap=cv2.VideoCapture(0)
#status of camera
while cap.isOpened():
    status,frame=cap.read()
    #detecting red color and saving in redimg
    redimg=cv2.inRange(frame,(0,0,0),(50,56,200))


    cv2.imshow("liveredcolor",redimg)
    if cv2.waitKey(10) & 0xff == ord("q"):
        break
cv2.destroyAllWindows()
cap.release()
