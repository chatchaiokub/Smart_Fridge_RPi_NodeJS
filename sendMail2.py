#!/usr/bin/python
import requests
import json
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)

state = 0
check = 0
start = 0

while True:

	b3 = GPIO.input(3)
	b4 = GPIO.input(4)
	b10 = GPIO.input(10)
	b25 = GPIO.input(25)
	b8 = GPIO.input(8)
	b15 = GPIO.input(15)
	
	sumb3 = 0
	sumb4 = 0
	sumb10 = 0
	sumb25 = 0
	sumb8 = 0
	sumb15 = 0
	total = 0

	
	if (b3 == False):
		sumb3 = 1
	if (b4 == False):
                sumb4 = 1
	if (b10 == False):
               	sumb10 = 1
	if (b25 == False):
               	sumb25 = 1
	if (b8 == False):
               	sumb8 = 1
	if (b15 == False):
               	sumb15 = 1
	if (b3 == True):
               	sumb3 = 0
     	if (b4 == True):
               	sumb4 = 0
        if (b10 == True):
               	sumb10 = 0
        if (b25 == True):
               	sumb25 = 0
        if (b8 == True):
               	sumb8 = 0
        if (b15 == True):
               	sumb15 = 0
	total = sumb3+sumb4+sumb10+sumb25+sumb8+sumb15
	print total
	time.sleep(1)
	
	if (total <= 1):
		state = 1

	if (total > 1):
		state = 0
		check = 0
		start = 1
		
	if (start == 1):
		if (check == 0):
			if (state == 1):
				print "Sented!"
				check = 1
