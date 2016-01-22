# Copyright 2016 PuurIDee
# Author Mark Nijboer

import os
import pygame
import random
import RPi.GPIO as GPIO

from time import sleep

# Board IO Pin for sensor
sensorPin = 10;

# Initialize pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensorPin, GPIO.IN)

# Loop
while 1:
  # If sensor port is HIGH
  if not GPIO.input(sensorPin):
    # Get random file from 'sounds' folder
    directory = "sounds/"
    soundFile = random.choice(os.listdir(directory))

    # Initialize player
    pygame.mixer.init()

    # Play sound
    pygame.mixer.music.load(directory+soundFile)
    pygame.mixer.music.play()

    # Wait until sound ends playing
    while pygame.mixer.music.get_busy() == True:
      continue

    # Uninitialize player to prevent hizz noise
    pygame.mixer.stop()
