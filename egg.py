#!/usr/bin/python
import requests
import json
import spidev
import time

channel = 0

#Create SPI
spi = spidev.SpiDev()
spi.open(0, 0)

temp = 0
count = 0
send = 1

def analogRead(data):

    	if data > 7 or data < 0:
        	return -1

    	r = spi.xfer2([1, 8 + data << 4, 0])
    	data = ((r[1] & 3) << 8) + r[2]

    	return data

def sendDataEGG(data):

	global temp
	global count
        global send
	if(data != temp):
		temp = data
		count = 0
	else:
		count = count+1

	if(count == 3):
		print ("Sending..... ",data)
		url = 'http://localhost:3000/dataEgg'
       		headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
		payload = {'egg': data}
        	response = requests.post(url,data=payload)
		
		if(data == 2 and send == 1):
			url = 'http://localhost:3000/setupEgg'
                	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
                	response = requests.get(url,headers=headers)
			send = 0

		elif(data != 2):
			send = 1	


global temp
global count
global send
while True:

    	val = analogRead(channel)
	time.sleep(0.5)

	print val

	if val > 1020:
		print ("No",val)
		sendDataEGG(0)
    	elif val <= 1020 and val >= 1005:
		print ("1 egg",val)
		sendDataEGG(1)
    	elif val <= 1004 and val >= 993:
        	print ("2 egg",val)
		sendDataEGG(2)
	elif val <= 992 and val >= 981:
                print ("3 egg",val)
	        sendDataEGG(3)
	elif val <= 980 and val >= 970:
                print ("4 egg",val)
		sendDataEGG(4)
	elif val <= 969 and val >= 961:
                print ("5 egg",val)
		sendDataEGG(5)
	elif val <= 960 and val >= 952:
                print ("6 egg",val)
		sendDataEGG(6)
	elif val <= 951 and val >= 944:
                print ("7 egg",val)
		sendDataEGG(7)
	elif val <= 943 and val >= 936:
                print ("8 egg",val)
		sendDataEGG(8)
	elif val <= 935 and val >= 927:
                print ("9 egg",val)
	        sendDataEGG(9)
	elif val <= 926 and val >= 918:
                print ("10 egg",val)
	        sendDataEGG(10)
