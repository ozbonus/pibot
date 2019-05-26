import RPi.GPIO as GPIO
import pygame
import pygame.display
import time
import os

# ########## # 
# GPIO Setup #
# ########## #

# Set pin numbering scheme.
GPIO.setmode(GPIO.BOARD)

# Set pins to output signals.
GPIO.setup(7,  GPIO.OUT) # Left wheel backward.
GPIO.setup(11, GPIO.OUT) # Left wheel forward.
GPIO.setup(13, GPIO.OUT) # Right wheel forward.
GPIO.setup(15, GPIO.OUT) # Right wheel backward.

# Software-defined pulse width modulation.
left_backward_pwm = GPIO.PWM(7, 100)
left_forward_pwm = GPIO.PWM(11, 100)
right_forward_pwm = GPIO.PWM(13, 100)
right_backward_pwm = GPIO.PWM(15, 100)

# ############ #
# pygame Setup #
# ############ #

pygame.init()
os.environ['SDL_VIDEODRIVER'] = 'dummy'
pygame.display.init()
screen = pygame.display.set_mode((100, 100))

# ################ #
# Controller Logic #
# ################ #

def forward(duty=100, seconds=None):
    left_forward_pwm.start(duty)
    right_forward_pwm.start(duty)
    if seconds:
        time.sleep(seconds)
        stop()
        time.sleep(0.2)

def backward(duty=100, seconds=None):
    left_backward_pwm.start(duty)
    right_backward_pwm.start(duty)
    if seconds:
        time.sleep(seconds)
        stop()
        time.sleep(0.2)

def left(duty=55, seconds=None):
    # Cheap motors require a little push at full power.
    right_forward_pwm.start(100)
    left_backward_pwm.start(100)
    time.sleep(0.1)
    right_forward_pwm.ChangeDutyCycle(duty)
    left_backward_pwm.ChangeDutyCycle(duty)
    if seconds:
        time.sleep(seconds)
        stop()
        time.sleep(0.2)

def right(duty=55, seconds=None):
    # Cheap motors require a little push at full power.
    right_backward_pwm.start(100)
    left_forward_pwm.start(100)
    time.sleep(0.1)
    right_backward_pwm.ChangeDutyCycle(duty)
    left_forward_pwm.ChangeDutyCycle(duty)
    if seconds:
        time.sleep(seconds)
        stop()
        time.sleep(0.2)

def stop():
    left_backward_pwm.stop()
    left_forward_pwm.stop()
    right_forward_pwm.stop()
    right_backward_pwm.stop()

def dance():
    forward(seconds=0.5)
    forward(seconds=0.5)
    backward(seconds=0.5)
    backward(seconds=0.5)
    left(duty=100, seconds=0.5)
    right(duty=100, seconds=1.5)
    right(duty=100, seconds=0.5)
    left(duty=100, seconds=1.5)

running = True

while running:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                GPIO.cleanup()
                pygame.quit()
            if event.key == pygame.K_UP:
                forward()
            if event.key == pygame.K_DOWN:
                backward()
            if event.key == pygame.K_LEFT:
                left()
            if event.key == pygame.K_RIGHT:
                right()
            if event.key == pygame.K_SPACE:
                dance()

# ######## #
# Clean Up #
# ######## #

GPIO.cleanup()
pygame.quit()
