from time import sleep

import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
while 1:
    GPIO.output(8, False)
    sleep(1)
    GPIO.output(8, True)
    sleep(1)
