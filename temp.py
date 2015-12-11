#!/usr/bin/env python

dev='/sys/bus/w1/devices/28-000005aae9fc/w1_slave'
print float(open(dev).readlines()[1].split('=')[1])/1000
