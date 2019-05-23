import curses
import RPi.GPIO as GPIO
import time

screen = curses.initscr()
#curses.noecho()
curses.cbreak()
curses.delay_output(900)
screen.keypad(True)

# Tell the Raspberry Pi what the pins will do.
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

# FUNCTION             | PIN
# -------------------------
# Left wheel forward   | 7
# Left wheel backward  | 11
# Right wheel forward  | 13
# Right wheel backward | 15

def lf(): GPIO.output(11, True)
def lb(): GPIO.output(7, True)
def rf(): GPIO.output(13, True)
def rb(): GPIO.output(15, True)
def tl(): lb(); rf()
def tr(): lf(); rb()
def stop(): GPIO.output([7, 11, 13, 15], False)

tl()
time.sleep(2)
stop()

tr()
time.sleep(2)
stop()


curses.nocbreak()
screen.keypad(False)
curses.echo()
curses.endwin()
GPIO.cleanup()
