import time
import ultrasonic as us
import infrared as ir
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

distance = 0
detect = 0
motion_detect = 0 
sensor = 0
LED = 14
GPIO.setup(LED,GPIO.OUT)

while True:
    motion_detect = ir.motion_detect(detect)
    if motion_detect == 1: 
        distance=us.reading(sensor)
        print("distance:"+str(distance))
        if distance<30:
            GPIO.output(LED,1)
        elif distance > 400:
            print("error")
        else:
            GPIO.output(LED,0)
