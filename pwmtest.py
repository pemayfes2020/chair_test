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
p = GPIO.PWM(in1, 50)  # 周波数50Hz
p.start(0)
#duty比
duty = 20

try:
    while True:
        # 正転
        p.ChangeDutyCycle(duty)
        #GPIO.output(in1, 1)
        GPIO.output(in2, 0)
        GPIO.output(in3, 0)
        GPIO.output(in4, 1)
        time.sleep(0.2)

except KeyboardInterrupt:
    pass

# ブレーキ
p.stop()
#GPIO.output(in1, 0)
GPIO.output(in2, 0)
GPIO.output(in3, 1)
GPIO.output(in4, 1)
time.sleep(0.1)
GPIO.cleanup()