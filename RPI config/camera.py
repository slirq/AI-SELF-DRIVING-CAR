
import time
import cv2


def main():
	cam=cv2.VideoCapture(-1)
	ret, frame = cam.read()
	frame = cv2.resize(frame,(128,128))
	return cam
def display():
	main()
	cam= cv2.VideoCapture(-1)
	ret, frame = cam.read()
	return cv2.imshow("cam",frame)
def end():
    #ini(cam)
    cam.release()
    cv2.destroyAllWindows()


def take_picture():
    current_date = (time.strftime("%d-%m-%Y"))
    current_time = (time.strftime("%H-%M-%S"))
    image_name = current_date + "_" + current_time + ".jpg"
    cv2.imwrite(image_name,frame)


def take_picture_test():
   cam=cv2.VideoCapture(-1)
   ret, frame = cam.read()
   img = cv2.resize(frame,(128,128))
   cv2.imwrite("test.jpg",img)
   cv2.imwrite("teststop.jpg",frame)
