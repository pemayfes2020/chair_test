# coding: UTF-8
import RPi.GPIO as GPIO
import time
import sys

#　ピン設定
i1=20
i2=21
in1=12
in2=18
in3=19
in4=13
encoder_green=0
encoder_yellow=0

GPIO.setmode(GPIO.BCM)
GPIO.setup(i1, GPIO.IN)
GPIO.setup(i2, GPIO.IN)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)

encoder_green_1=0
encoder_yellow_1=0
count=0 
#count0=0
i=0
GPIO.output(in1,0)
GPIO.output(in2,1)
GPIO.output(in3,1)
GPIO.output(in4,0)

# エンコーダ読み取り
# 4逓倍
try:
    while count <44*21.3*10 and count > -44*21.3:
        
        encoder_green=GPIO.input(i1)
        encoder_yellow=GPIO.input(i2)
        if(encoder_green_1==0 and encoder_yellow_1==0):
            if(encoder_green==1 and encoder_yellow==0):
                count+=1
            if(encoder_green==0 and encoder_yellow==1):
                count-=1
        elif(encoder_green_1==1 and encoder_yellow_1==0):
            if(encoder_green==1 and encoder_yellow==1):
                count+=1
            if(encoder_green==0 and encoder_yellow==0):
                count-=1
        elif(encoder_green_1==1 and encoder_yellow_1==1):
            if(encoder_green==0 and encoder_yellow==1):
                count+=1
            if(encoder_green==1 and encoder_yellow==0):
                count-=1
        elif(encoder_green_1==0 and encoder_yellow_1==1):
            if(encoder_green==0 and encoder_yellow==0):
                count+=1
            if(encoder_green==1 and encoder_yellow==1):
                count-=1
        encoder_green_1=encoder_green
        encoder_yellow_1=encoder_yellow
        #if(count!=count0):
        i+=1
        #count0=count
        #print(count) 
        print(encoder_green, encoder_yellow,count,i)

except KeyboardInterrupt:
    pass
GPIO.output(in1,1)
GPIO.output(in2,1)
GPIO.output(in3,0)
GPIO.output(in4,0)
time.sleep(0.5)

GPIO.cleanup()