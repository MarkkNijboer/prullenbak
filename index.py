

import os
import random
import pygame

from time import sleep
import RPi.GPIO as GPIO

# Board IO Pin for sensor
sensorPin = 8;

# Initialize pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensorPin, GPIO.IN)

# Initialize sound
pygame.mixer.init()

# Loop
while 1:
    # If sensor port is HIGH
    if GPIO.input(sensorPin):
        # Get random file from 'sounds' folder
        directory = "sounds/"
        soundFile = random.choice(os.listdir(directory))

        # Play sound
        pygame.mixer.music.load(directory+soundFile)
        pygame.mixer.music.play()

        # Wait until sound ends playing
        while pygame.mixer.music.get_busy() == True:
            continue
