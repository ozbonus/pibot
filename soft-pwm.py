import RPi.GPIO as GPIO
import pygame
import time
import os

# ##########
# GPIO Setup
# ##########

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,  GPIO.OUT) # Left wheel backward.
GPIO.setup(11, GPIO.OUT) # left wheel forward.
GPIO.setup(13, GPIO.OUT) # Right wheel forward.
GPIO.setup(15, GPIO.OUT) # Right wheel backward.

duty = 0
p1 = GPIO.PWM(11, 100)
p1.start(duty)

while True:
    print('\nCurrent duty cycle: {}'.format(duty))
    print('Enter a new duty cycle between 0.0 and 100.0')
    print('Other values will exit the script.')
    duty = input('New duty cycle: ')
    try:
        p1.ChangeDutyCycle(float(duty))
    except:
        break

GPIO.cleanup()
