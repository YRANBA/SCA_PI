#!/usr/bin/env python
import random

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

buzz_pin=32

led_pin = 11


GPIO.setup(buzz_pin, GPIO.OUT)
GPIO.setup(led_pin, GPIO.OUT)

Buzz = GPIO.PWM(buzz_pin, 1000)
Buzz.ChangeFrequency(440)
n= random.randint(1,1000)


while True:
	guess = int(raw_input('guess a number from 1-10'))
	if guess < n:
		Buzz.start (50)
		time.sleep(1)
		print 'guess is too low'
	
	elif guess > n:
		Buzz.start (50)
		time.sleep(1)
		print 'guess is too high'

			
	else:
		GPIO.output (led_pin, True)
		time.sleep(2)
		GPIO.output(led_pin, False)
		GPIO.cleanup()
		print 'you guessed it'
		break
