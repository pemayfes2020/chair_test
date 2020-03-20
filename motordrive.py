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

# 正転
GPIO.output(in1, 1)
GPIO.output(in2, 0)
GPIO.output(in3, 0)
GPIO.output(in4, 1)
time.sleep(5.0)

# ブレーキ
GPIO.output(in1, 1)
GPIO.output(in2, 1)
GPIO.output(in3, 0)
GPIO.output(in4, 0)
time.sleep(1.1)

# 後転
GPIO.output(in1, 0)
GPIO.output(in2, 1)
GPIO.output(in3, 1)
GPIO.output(in4, 0)
time.sleep(0.7)

# ブレーキ
GPIO.output(in1, 1)
GPIO.output(in2, 1)
GPIO.output(in3, 0)
GPIO.output(in4, 0)
time.sleep(0.1)
GPIO.cleanup()