#from time import sleep

#import RPi.GPIO as GPIO


#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(8, GPIO.OUT)
#while 1:
#    GPIO.output(8, False)
#    sleep(1)
#    GPIO.output(8, True)
#    sleep(1)

import os, random
import pygame

directory = "sounds/"
soundFile = random.choice(os.listdir(directory))

pygame.mixer.init()
pygame.mixer.music.load(directory+soundFile)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
