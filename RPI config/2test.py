

import movement
import os
import time
import stop
import h5py
import numpy as np
from keras.models import load_model
from keras.models import Model
from PIL import Image
import cv2


print("Wait please")
p = 0
tf = 2

movement.init()
model = load_model('my_model74.h5')
print("Camera initialized, go ahead!")
cap = cv2.VideoCapture(-1)


if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    img = cv2.resize(frame,(128,128))
    cv2.imwrite("test.jpg",img)
    #cv2.imwrite("teststop.jpg",frame)
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imshow('Input', frame)
    cv2.imwrite("teststop.jpg",frame)
    stops = stop.detect()
    if stops is True:
        print('loop')
        #movement.pause()
        continue
    elif stops is False:
        image = Image.open('test.jpg')
        image = np.array(image)
        p = model.predict(np.expand_dims(image, axis=0))
        print(p)
        p = np.argmax(p, axis = 1)
        p=p[0]

        if p == 0:
            movement.left()
            #movement.pause()
            print("left")

        elif p == 1:
            movement.forward()
            print("forward")

        elif p == 2:
            movement.right()
            print("right")
            #movement.pause()

        elif p == 3:
            print("quit")
            movement.pause()
    #movement.pause()
    #time.sleep(0.3)
    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()

