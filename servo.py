#!/usr/bin/env python

import RPi.GPIO as GPIO
from sys import argv, stdin, stderr, exit
from time import sleep
from math import isinf, isnan

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

OPEN = 6.0
CLOSED = 11.0

p = GPIO.PWM(7, 50)

def convert(str):
    if str.lower() == 'open':
        return OPEN
    if str.lower() == 'close':
        return CLOSED

    duty = float(str)

    if isinf(duty):
        raise ValueError('duty cycle can not be Inf')
    if isnan(duty):
        raise ValueError('duty cycle can not be Nan')
    if duty < 0.0 or duty > 100.0:
        raise ValueError('duty cycle out of range')

    return duty

try:
    if len(argv) == 2: # set to arg
        p.start(convert(argv[1]))
        sleep(0.5)

    else: # read multiple values from stdin
        p.start(OPEN)
        while True: # for unbuffered reads
            p.ChangeDutyCycle(convert(stdin.readline().rstrip('\n')))

finally:
    p.stop()
    GPIO.cleanup()
