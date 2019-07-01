#!/usr/bin/python3
import cv2
#calling classifier
casclf=cv2.CascadeClassifier('face.xml') #dir(casclf) for mor info
#loading face data
cap=cv2.VideoCapture(0) 
while cap.isOpened():
    status,frame=cap.read()
    # now we can apply classifier in live frame
    face=casclf.detectMultiScale(frame,1.5,5) # classifier tuning parameter ---> 1.13
    #print(face)
    # for loop is additional for face detection
    for x,y,h,w in face: #innitial conrdinate (x,y), hight, width
        cv2.rectangle(frame,(x,y),(x+h,y+w),(0,0,255),2) # to move rectangle with face detected on screen
        #only face 
        #facedata=frame[x:x+h,y:y+w]
        cv2.imshow('f',frame)

    #cv2.imshow('face',frame)
    if( cv2.waitKey(10) & 0xff == ord('q')):
        break
cv2.destroyAllWindows()
cap.release()

