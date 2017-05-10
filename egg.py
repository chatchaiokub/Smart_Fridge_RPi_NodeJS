#!/usr/bin/python
import requests
import json
import spidev
import time

ldr_channel = 0

#Create SPI
spi = spidev.SpiDev()
spi.open(0, 0)
 
def analogRead(data):

    	if data > 7 or data < 0:
        	return -1

    	r = spi.xfer2([1, 8 + data << 4, 0])
    	data = ((r[1] & 3) << 8) + r[2]

    	return data

def sendData(data):
	print ("Have",data)
	url = 'http://localhost:3000/dataegg'
       	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
	payload = {'egg': data}
        response = requests.post(url,data=payload)

check = -1

while True:

    	val = analogRead(ldr_channel)
	time.sleep(0.5)


    	if val >= 1006:
		print ("No",val)
		check = 0	
		if (check == 1):
			check = 0
			sendData(0)
		elif (check == 0):
			check = 0
		elif (check == -1):
			check = 0
			sendData(0)
    	elif val < 1005 and val >= 980:
		print ("1 egg",val)
		
		if (check == 0):
			check = 1
			sendData(1)
		elif (check == 1):
			check = 1
		else:
                        check = 1
                        sendData(1)

    	elif val <= 979 and val >= 955:
        	print ("2 egg",val)
		
		if (check == 1):
                        check = 2
                        sendData(2)
                elif (check == 2):
                        check = 2
		else:
			check = 2
			sendData(2)
    	elif val <= 954 and val >= 935:
        	print ("3 egg",val)
		
		if (check == 2):
                        check = 3
                        sendData(3)
                elif (check == 3):
                        check = 3
	
