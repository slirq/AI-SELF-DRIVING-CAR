# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 17:56:37 2019

@author: abdul
"""


import cv2
forward_counter = 0
right_counter = 0
left_counter = 0
blank_counter = 0
def forward(cam):
    count = 0
    global forward_counter
    while count<5:
        ret,frame = cam.read()
        if not ret:
            break
        img1 = cv2.resize(frame,(128,128))
        img_name = "C:\\Users\\abdul\\Desktop\\autocar\\Self-driving-car-master\\images2\\w\\pose_test2_{}.png".format(forward_counter)
            
        cv2.imwrite(img_name, img1)
        print("{} written!".format(img_name))
        forward_counter += 1
        count += 1
    return
        
    
        
def right(cam):
    count = 0
    global right_counter    
    while count<5:
        ret,frame = cam.read()
        img1 = cv2.resize(frame,(128,128))
        img_name = "C:\\Users\\abdul\\Desktop\\autocar\\Self-driving-car-master\\images2\\d\\pose_test2_{}.png".format(right_counter)
            
        cv2.imwrite(img_name, img1)
        print("{} written!".format(img_name))
        right_counter += 1
        count += 1
    return
        
def left(cam):
    count = 0
    global left_counter    
    while count<5:
        ret,frame = cam.read()
        img1 = cv2.resize(frame,(128,128))
        img_name = "C:\\Users\\abdul\\Desktop\\autocar\\Self-driving-car-master\\images2\\a\\pose_test2_{}.png".format(left_counter)
            
        cv2.imwrite(img_name, img1)
        print("{} written!".format(img_name))
        left_counter += 1
        count += 1
    return

def blank(cam):
    count = 0
    global blank_counter
    while count<5:
        ret,frame = cam.read()
        if not ret:
            break
        img1 = cv2.resize(frame,(128,128))
        img_name = "C:\\Users\\abdul\\Desktop\\autocar\\Self-driving-car-master\\images2\\q\\pose_test2_{}.png".format(blank_counter)
            
        cv2.imwrite(img_name, img1)
        print("{} written!".format(img_name))
        blank_counter += 1
        count += 1
    return


cam = cv2.VideoCapture(1)
cv2.namedWindow("test")

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
   
        # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        # gray = cv2.GaussianBlur(gray,(21,21),0)
        # img1 = cv2.resize(frame,(128,128))
    if not ret:
        break
    k = cv2.waitKey(1)
        
        
    if k%256 == 27:
            #esc
        print("Escape hit, closing...")
        break
    elif k%256 == 119:
            #w
        forward(cam)
        
    elif k%256 == 97:
            #a
        left(cam)
            
    elif k%256 == 100:
        #d
        right(cam)
    elif k%256 == 32:
        #spacebar
        blank(cam)
                
                
                #count = 0
            
                #while count<5:
                # ret,frame = cam.read()
                # img1 = cv2.resize(frame,(128,128))
                #  img_name = "C:\\Users\\abdul\\Desktop\\autocar\\Self-driving-car-master\\images2\\video\\pose_test2_{}.png".format(img_counter)
                
                #cv2.imwrite(img_name, img1)
                #print("{} written!".format(img_name))
                #img_counter += 1
            #count += 1
            #flip = cv2.flip(frame,1)
            #cv2.imshow("flip", flip) 
    
        
cam.release()
cv2.destroyAllWindows()



