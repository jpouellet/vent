#!/usr/bin/env python

import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

ports = (18, 16, 11, 12, 13, 15)

for port in ports:
	GPIO.setup(port, GPIO.OUT)
	GPIO.output(port, GPIO.LOW)

n = int(float(sys.argv[1]))

for i in xrange(0, len(ports)):
	GPIO.output(ports[i], n & (1 << i))
