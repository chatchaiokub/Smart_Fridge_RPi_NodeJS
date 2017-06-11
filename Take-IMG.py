#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

#------------------------

LDR = 4

#------------------------

def RCtime (LDR):

  reading = 0

  GPIO.setup(LDR, GPIO.OUT)
  GPIO.output(LDR, GPIO.LOW)
  time.sleep(0.1)

  GPIO.setup(LDR, GPIO.IN)
  while (GPIO.input(LDR) == GPIO.LOW):
    reading += 1
  return reading

#---------------------------------------

def on():
	GPIO.setup(17, GPIO.OUT)
	GPIO.output(17, GPIO.LOW)
def off():
	GPIO.setup(17, GPIO.OUT)
	GPIO.output(17, GPIO.HIGH)

#--------------------------------------
z = 1
line = 0
LINE = 0
while True:

 if z==0:
  if RCtime(LDR) > 2000:
   off()
   time.sleep(2)
   os.system ("fswebcam -d /dev/video0 -r 1280x780 --no-banner ./public/Front1.jpg")
   os.system ("fswebcam -d /dev/video1 -r 1280x780 --no-banner ./public/Front2.jpg")
   time.sleep(3)
   on()
   GPIO.setup(3, GPIO.OUT)
   GPIO.output(3,GPIO.LOW)	#alert led when don't close the door
   z=1
   LINE = 0
  else:
   on()
   line = 1
   if line == 1:
    LINE += line
   if LINE == 20:
    os.system ("python Alertdoor.py")
 elif z==1:
  if RCtime(LDR) < 1000:
   z = 0 
   time.sleep(2)  
   os.system ("fswebcam -d /dev/video2 -r 1280x780 --no-banner ./public/Back.jpg")
   GPIO.setup(3, GPIO.OUT)
   GPIO.output(3,GPIO.HIGH)	#alert led when don't close the door
   	
  else:
   on()
   line = 0
 
 #if RCtime(LDR) < 1000:
  #line = 1
  #if line == 1:
  # LINE += line
  #if LINE == 40:
  # os.system ("python Alertdoor.py")
  # LINE = 0
  
 print RCtime(LDR)
