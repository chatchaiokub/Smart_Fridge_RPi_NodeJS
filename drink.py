#!/usr/bin/python
import requests
import json
import spidev
import time

channel = 1

#Create SPI
spi = spidev.SpiDev()
spi.open(0, 0)

temp = 0
count = 0

def analogRead(data):

    	if data > 7 or data < 0:
        	return -1

    	r = spi.xfer2([1, 8 + data << 4, 0])
    	data = ((r[1] & 3) << 8) + r[2]

    	return data

def sendDataDRINK(data):

	global temp
	global count

	if(data != temp):
		temp = data
		count = 0
	else:
		count = count+1
	if(count == 3):
		print ("Sending..... ",data)
		url = 'http://localhost:3000/dataDrink'
       		headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
		payload = {'drink': data}
        	response = requests.post(url,data=payload)

check = -1
global temp
global count

while True:

    	val = analogRead(channel)
	time.sleep(0.5)

	print val

    if val > 1020:
		        print ("No",val)
		        sendDataDRINK(0)
    elif val <= 1019 and val >= 1012:
		        print ("1 drink",val)
		        sendDataDRINK(1)
    elif val <= 1011 and val >= 1004:
        	    print ("2 drink",val)
		        sendDataDRINK(2)
	elif val <= 1003 and val >= 997:
                print ("3 drink",val)
	            sendDataDRINK(3)
	elif val <= 996 and val >= 991:
                print ("4 drink",val)
        		#	url = 'http://localhost:3000/setupEgg'
        		#	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        		#	response = requests.get(url,headers=headers)
		        sendDataDRINK(4)
	elif val <= 990 and val >= 983:
                print ("5 drink",val)
		        sendDataDRINK(5)
	elif val <= 982 and val >= 976:
                print ("6 drink",val)
		        sendDataDRINK(6)
	elif val <= 975 and val >= 968:
                print ("7 drink",val)
		        sendDataDRINK(7)
	elif val <= 969 and val >= 964:
                print ("8 drink",val)
		        sendDataDRINK(8)
	elif val <= 963 and val >= 957:
                print ("9 drink",val)
		        sendDataDRINK(9)
	elif val <= 956 and val >= 952:
                print ("10 drink",val)
                sendDataDRINK(10)
	elif val <= 953 and val >= 949:
                print ("11 drink",val)
                sendDataDRINK(11)
	elif val <= 948 and val >= 943:
                print ("12 drink",val)
                sendDataDRINK(12)
