import RPi.GPIO as GPIO
import time
import pygame

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)  # Left wheel backward.
GPIO.setup(11, GPIO.OUT) # Left wheel forward.
GPIO.setup(13, GPIO.OUT) # Right wheel forward.
GPIO.setup(15, GPIO.OUT) # Right wheel backward.

def forward(): GPIO.output([11, 13], True)
def backward(): GPIO.output([7, 15], True)
def left(): GPIO.output([7, 13], True)
def right(): GPIO.output([11, 15], True)
def stop(): GPIO.output([7, 11, 13, 15], False)

forward()
time.sleep(2)
stop()

backward()
time.sleep(2)
stop()

left()
time.sleep(2)
stop()

right()
time.sleep(2)
stop()

GPIO.cleanup()
