import numpy as np 
import cv2


face_cascade = cv2.CascadeClassifier('/home/pi/robotics/autocar/StopSign_HAAR/Stopsign_HAAR_19Stages.xml')




cap = cv2.VideoCapture(-1)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray,(128,128))
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if faces !=():
        print(1)
    #print(faces)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
    else:
        print(0)

    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
