def motion_detect(detect):
    import RPi.GPIO as GPIO
    import time
    ### setup
    LED = 14
    TRIG = 18
    GPIO.setup(TRIG, GPIO.IN) # GPIO 18 : human detect sensor
    GPIO.setup(LED, GPIO.OUT) # GPIO 6: LED

    # initialize
    #if GPIO.input(18):
      #GPIO.output(14, 1)
    #else:
      #GPIO.output(14, 0)
    if detect == 0:
      GPIO.wait_for_edge(TRIG, GPIO.BOTH)
      if GPIO.input(TRIG):
        print("detected!")
        GPIO.output(LED, 1)
        return 1
      else:
        GPIO.output(LED, 0)
        return 0
      GPIO.cleanup()
    else:
      print("failed")