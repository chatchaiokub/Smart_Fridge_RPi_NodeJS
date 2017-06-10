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
send = 1
def analogRead(data):

    	if data > 7 or data < 0:
        	return -1

    	r = spi.xfer2([1, 8 + data << 4, 0])
    	data = ((r[1] & 3) << 8) + r[2]

    	return data

def sendDataDRINK(data):

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
		url = 'http://localhost:3000/dataDrink'
       		headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
		payload = {'drink': data}
        	response = requests.post(url,data=payload)
		
		if(data == 4 and send == 1):
                        url = 'http://localhost:3000/setupDrink'
                        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
                        response = requests.get(url,headers=headers)
                        send = 0

                elif(data != 4):
                        send = 1
global send
global temp
global count

while True:

    	val = analogRead(channel)
	time.sleep(0.5)

	print val

    	if val > 1020:
	        print ("No",val)
	        sendDataDRINK(0)
    	elif val <= 1020 and val >= 1005:
	        print ("1 drink",val)
	        sendDataDRINK(1)
    	elif val <= 1004 and val >= 990:
       		print ("2 drink",val)
	        sendDataDRINK(2)
	elif val <= 989 and val >= 975:
                print ("3 drink",val)
	        sendDataDRINK(3)
	elif val <= 974 and val >= 964:
                print ("4 drink",val)
		sendDataDRINK(4)
	elif val <= 963 and val >= 953:
                print ("5 drink",val)
	        sendDataDRINK(5)
	elif val <= 952 and val >= 942:
                print ("6 drink",val)
	        sendDataDRINK(6)
	elif val <= 941 and val >= 930:
                print ("7 drink",val)
	        sendDataDRINK(7)
	elif val <= 929 and val >= 921:
                print ("8 drink",val)
	        sendDataDRINK(8)
	elif val <= 920 and val >= 911:
                print ("9 drink",val)
	        sendDataDRINK(9)
	elif val <= 910 and val >= 901:
                print ("10 drink",val)
                sendDataDRINK(10)
	elif val <= 900 and val >= 895:
                print ("11 drink",val)
                sendDataDRINK(11)
	elif val <= 894 and val >= 882:
                print ("12 drink",val)
                sendDataDRINK(12)
