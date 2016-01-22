# Copyright 2016 PuurIDee
# Author Mark Nijboer

import os
import pygame
import random
import RPi.GPIO as GPIO
import signal
import sys

from threading import Lock
from time import sleep

# Board IO Pin for sensor
sensorPin = 10;
# Setup lock
irq_lock = Lock(False)

# Interrupt Service Routine
def playSound(channel):
  if not irq_lock.acquire():
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
    # Release lock
    irq_lock.release()

# Catch Keyboardinterrupt to cleanup GPIO channels
def signal_handler(signal, frame):
  print("Called!");
  GPIO.cleanup()
  sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


# Initialize pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Setup interrupt
GPIO.add_event_detect(sensorPin, GPIO.FALLING, callback=playSound)

# Infinite loop
while True:
    sleep(1)
