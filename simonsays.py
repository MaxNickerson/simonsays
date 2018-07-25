import RPi.GPIO as GPIO
import LEDRGB as LED
import time
import random
from getpass import getpass
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
buzz_pin = 32
GPIO.setup(buzz_pin, GPIO.OUT)
Buzz = GPIO.PWM(buzz_pin, 1000)
colorlist  = []
soundlist = []
colorstring = colorlist

colors = ['R', 'G', 'B', 'Y','P']
frequencies = [220, 400, 600, 800, 840]
#frequencies = [23578000, 2358923525, 23523523325235, 23523523235235235235235, 2358908902358902350]
#frequencies = [12250, 1241241, 8930, 15899, 901]
#frequencies = [12000, 12200, 12500, 12900, 13020]
R_pin = 11
G_pin = 12
B_pin = 13
LED.setup(R_pin, G_pin, B_pin)

def validate_guess(colorlist, guess):
	if colorlist == guess:
		print "Keep er goin"
	else:
		print "Game over"
		print colorlist, "was the correct sequence"
		print guess, "was your guess"
		exit()


def simonsays():
	print "Input the color sequence like: rbbgygp \nr = red, b = blue, g = green, y = yellow, and p = pink"
	while True:
		n = random.randint(0,4)
		colorlist.append(colors[n])
		soundlist.append(frequencies[n])
		p = len(colorlist)
		x = 0
		while p > 0:
			LED.setColor(colorlist[x])
			Buzz.ChangeFrequency(soundlist[x])
			Buzz.start(1)
			time.sleep(.5)
			Buzz.stop()
			LED.noColor()
			#time.sleep(1)
			p = p - 1
			x = x + 1
		guess = getpass("Guess the color sequence: ")
		colorstring = ''.join(colorlist)
		validate_guess(colorstring,guess.upper())
		
			
		

		
				
			
			
	
if __name__ == '__main__':
	try:
		simonsays()
	except KeyboardInterrupt:
		print 'Good bye'
		LED.destroy()
