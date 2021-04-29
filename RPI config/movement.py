

import RPi.GPIO as gpio
import time


def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)

    global s, e, t, f
    s = gpio.PWM(7, 50)
    e = gpio.PWM(11, 50)
    t = gpio.PWM(13, 50)
    f = gpio.PWM(15, 50)

    s.start(0)
    e.start(0)
    t.start(0)
    f.start(0)


def end():
    s.stop()
    e.stop()
    t.stop()
    f.stop()

def reverse():
    s.ChangeDutyCycle(0)
    e.ChangeDutyCycle(40)
    t.ChangeDutyCycle(40)
    f.ChangeDutyCycle(0)

def forward():
    s.ChangeDutyCycle(55)
    e.ChangeDutyCycle(0)
    t.ChangeDutyCycle(0)
    f.ChangeDutyCycle(55)
    #time.sleep(0.2)
def right():
    s.ChangeDutyCycle(0)  # true
    e.ChangeDutyCycle(0) # true
    t.ChangeDutyCycle(0)  # true
    f.ChangeDutyCycle(65)
    #time.sleep(0.2)  # fals
def left():
    s.ChangeDutyCycle(65)  # false
    e.ChangeDutyCycle(0)  # true
    t.ChangeDutyCycle(0)  # false
    f.ChangeDutyCycle(0)
    #time.sleep(0.2)  # false
def pause():
    s.ChangeDutyCycle(0)  # false
    e.ChangeDutyCycle(0)  # true
    t.ChangeDutyCycle(0)  # false
    f.ChangeDutyCycle(0) 
