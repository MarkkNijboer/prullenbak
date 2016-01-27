import RPi.GPIO as GPIO

sensorPin = 10
# Initialize pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensorPin, GPIO.IN)

while True:
    print input(sensorPin)
