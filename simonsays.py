import RPi.GPIO as GPIO
import LEDRGB as LED
import time
import random
colors = ['R', 'G', 'B', 'Y','O']
R_pin = 11
G_pin = 12
B_pin = 13
LED.setup(R_pin, G_pin, B_pin)




def simonsays():
	while True:
		n = random.randint(0,4)
		LED.setColor(colors[n])
		time.sleep(0.25)
	
if __name__ == '__main__':
	try:
		simonsays()
	except KeyboardInterrupt:
		print 'Good bye'
		LED.destroy()
