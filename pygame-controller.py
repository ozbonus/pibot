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
# window = pygame.display.set_mode((100, 100))

os.environ['SDL_VIDEODRIVER'] = 'dummy'
pygame.display.init()
screen = pygame.display.set_mode((100, 100))

# ################ #
# Controller Logic #
# ################ #

def forward(duty=100):
    left_forward_pwm.start(duty)
    right_forward_pwm.start(duty)

def backward(duty=100):
    left_backward_pwm.start(duty)
    right_backward_pwm.start(duty)

def left(duty=60):
    right_forward_pwm.start(duty)
    left_backward_pwm.start(duty)

def right(duty=60):
    right_backward_pwm.start(duty)
    left_forward_pwm.start(duty)

def stop():
    left_backward_pwm.stop()
    left_forward_pwm.stop()
    right_forward_pwm.stop()
    right_backward_pwm.stop()

running = True

while running:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            stop()
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_SPACE:
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
        

# ######## #
# Clean Up #
# ######## #

GPIO.cleanup()
pygame.quit()
