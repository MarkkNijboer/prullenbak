import RPi.GPIO as GPIO

sensorPin = 10
GPIO.setup(sensorPin, GPIO.IN)

while True:
    print input(sensorPin)
