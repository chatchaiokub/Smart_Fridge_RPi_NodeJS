#!/usr/bin/python
import requests
import json
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

state = 0
start = 0
terminate = 1

while True:

	input_17 = GPIO.input(17)

    	if (input_17 == True):

        	state = 0	
		print state
        	time.sleep(1)

		if (start == 1):
			if (terminate == 1):

				url = 'http://localhost:3000/drink'
				headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
				response = requests.get(url,headers=headers)
				terminate = 0

	if (input_17 == False):
                state = 1
                print state
                time.sleep(1)
		start = 1
		terminate = 1
