import numpy as np
import cv2
cap = cv2.VideoCapture(0)
out = cv2.VideoWriter('ColorVideo.avi',-1,20.0, (640,480))
while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        out.write(frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
