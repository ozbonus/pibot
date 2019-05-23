import RPi.GPIO as GPIO
import pygame
import os

# ##########
# GPIO Setup
# ##########

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,  GPIO.OUT) # Left wheel backward.
GPIO.setup(11, GPIO.OUT) # left wheel forward.
GPIO.setup(13, GPIO.OUT) # Right wheel forward.
GPIO.setup(15, GPIO.OUT) # Right wheel backward.

def forward(): GPIO.output([11, 13], True)
def backward(): GPIO.output([7, 15], True)
def left(): GPIO.output([7, 13], True)
def right():
    GPIO.output([11, 15], True)
def stop(): GPIO.output([7, 11, 13, 15], False)
stop() # Sometimes the motors start automatically for some reason.

# ################
# Messing with PWM
# ################

# freq = 100
# duty = 65
# p1 = GPIO.PWM(11, freq)
# p2 = GPIO.PWM(15, freq)
# p1.start(duty)
# p2.start(duty)
# input('Press enter')
# p1.stop()
# p2.stop()

# ############
# Pygame Stuff
# ############

os.environ['SDL_VIDEODRIVER'] = 'dummy'
pygame.init()
window = pygame.display.set_mode((100, 100))

running = True

while running:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                forward()
            if event.key == pygame.K_DOWN:
                backward()
            if event.key == pygame.K_LEFT:
                left()
            if event.key == pygame.K_RIGHT:
                right()

GPIO.cleanup()
pygame.quit()
