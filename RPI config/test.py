

import movement
import camera
import os
import cv2
import time
import stop

import h5py
import numpy as np
from keras.models import load_model
from keras.models import Model
from PIL import Image


print("Wait please")
p = 0
#tf = 1.6
camera.main()
print("waait")
movement.init()
print('wait more')
model = load_model('my_modelnew.h5')
print("Camera initialized, go ahead!")
#cam = cv2.VideoCapture(-1)
#cv2.namedWindow("cam")
#out = cv2.VideoWriter('cam.avi',cv2.VideoWriter_fourcc('M','J','P','G'),10,(640,480))
while True:
    #camera.display()
    #cam= cv2.VideoCapture(-1)
    #ret,img = cam.read()
    #frame = cv2.resize(img,(128,128))
    #cv2.imwrite("test.jpg",frame)
    #cv2.imshow("cam",img) 
    #time.sleep(0.012)
    camera.take_picture_test()
    stops = stop.detect()
    if stops is True:
        print('loop')
        #movement.pause()
        continue
        
    elif stops is False:
        #camera.take_picture_test()
        image = Image.open('test.jpg')
        #image =cv2.imread("test.jpg")
        #out.write(image)
        image = np.array(image)
        p = model.predict(np.expand_dims(image, axis=0))
        print(p)
        p = np.argmax(p, axis = 1)
        p=p[0]
        if p == 0:
            movement.left()
            movement.pause()
            print("left")
        elif p == 1:
            movement.forward()
            #time.sleep(0.5)
            movement.pause()
            print("forward")
        elif p == 2:
            movement.right()
            movement.pause()
            print("right")
        elif p == 3:
            print("quit")
            continue
        #movement.end()
        #camera.end()
    #movement.pause()
#cam.release()
#cv2.destroyAllWindows()
#predict():
#    image = Image.open('test.jpg')
#        #image =cv2.imread("test.jpg")
#        #out.write(image)
#    image = np.array(image)
#    p = model.predict(np.expand_dims(image, axis=0))
#    print(p)
#    print('pred')
#    p = np.argmax(p, axis = 1)
#    p=p[0]
#    if p == 0:
#        movement.left()
#        print("left") 
#    elif p == 1:
#        movement.forward()
#        print("forward")
#    elif p == 2:
#        movement.right()
#        print("right")#
#    elif p == 3:
#        print("quit")
#        continue
   # movement.end()

