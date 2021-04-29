import numpy as np
import cv2
import movement

def detect():
    face_cascade = cv2.CascadeClassifier('/home/pi/robotics/autocar/StopSign_HAAR/Stopsign_HAAR_19Stages.xml')
    #cap = cv2.VideoCapture(-1)
    #ret, img = cap.read()
    img = cv2.imread('teststop.jpg')

    faces = face_cascade.detectMultiScale(img, 1.1, 3)
    if faces !=():
        print("stop")
    	#print(faces)
        movement.pause()
        #for (x, y, w, h) in faces:
         #   cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
         #   #roi_gray = gray[y:y + h, x:x + w]
          #  roi_color = img[y:y + h, x:x + w]
        return True
    else:
        return False
    cv2.destroyAllWindows

