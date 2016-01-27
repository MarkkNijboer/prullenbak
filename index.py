# Copyright 2016 PuurIDee
# Author Mark Nijboer

import os
import pygame
import random
import RPi.GPIO as GPIO
import signal
import sys
import time


# Board IO Pin for sensor
sensorPin = 8;
# Last time called
called = None

# Interrupt Service Routine
def playSound(channel):
  # Get 'called' into scope
  global called

  # Check whether last time called was at least a second ago
  if called is None or called <= time.time() - 1:
    # Get absolute path to 'sounds' folder
    directory = os.path.dirname(os.path.abspath(__file__))+"/sounds/"
    # Get random file from 'sounds' folder
    soundFile = random.choice(os.listdir(directory))

    # Initialize player
    pygame.mixer.init()

    # Play sound
    pygame.mixer.music.load(directory+soundFile)
    pygame.mixer.music.play()

    # Wait until sound stops playing
    while pygame.mixer.music.get_busy() == True:
      continue

    # Uninitialize player to prevent hizz noise
    pygame.mixer.stop()
    # Save current time
    called = time.time()

# Catch Keyboardinterrupt to cleanup GPIO channels
def signal_handler(signal, frame):
  GPIO.cleanup()
  sys.exit(0)
# Register Keyboardinterrupt
signal.signal(signal.SIGINT, signal_handler)


# Initialize pins
GPIO.setmode(GPIO.BOARD)
# Setup sensor pin and set rest mode to HIGH output.
GPIO.setup(sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# Register interrupt for a falling signal: HIGH -> LOW
GPIO.add_event_detect(sensorPin, GPIO.RISING, callback=playSound)

# Infinite loop
while True:
    time.sleep(1)
