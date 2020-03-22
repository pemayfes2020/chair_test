# coding: UTF-8
import RPi.GPIO as GPIO
import time
import sys
# ピン設定
in1=12
in2=18
in3=19
in4=13

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
pccw = GPIO.PWM(in1, 500)  # 周波数500Hz
pcw = GPIO.PWM(in2, 500)  # 周波数500Hz
pccw.start(0)
pcw.start(0)
#duty比
dutyccw = 90
dutycw = 90

try:
    while True:
        """
        # CCW
        pccw.ChangeDutyCycle(dutyccw)
        #GPIO.output(in1, 1)
        GPIO.output(in2, 0)
        GPIO.output(in3, 0)
        GPIO.output(in4, 1)
        time.sleep(0.2)
        """
        # CW
        GPIO.output(in1, 0)
        pcw.ChangeDutyCycle(dutycw)
        #GPIO.output(in2, 1)
        GPIO.output(in3, 1)
        GPIO.output(in4, 0)
        time.sleep(0.2)
        


except KeyboardInterrupt:
    pass

# ブレーキ
pccw.stop()
pcw.stop()
GPIO.output(in1, 0)
GPIO.output(in2, 0)
GPIO.output(in3, 1)
GPIO.output(in4, 1)
time.sleep(0.1)
GPIO.cleanup()