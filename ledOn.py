#!/usr/bin/python
import requests
import json
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)


GPIO.output(2,GPIO.HIGH)
time.sleep(1)
