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
		#if (check == 1):
		#	check = 0
		#	sendDataEGG(0)
		#elif (check == 0):
		#	check = 0
		#elif (check == -1):
		#	check = 0
		#	sendDataEGG(0)
		sendDataDRINK(0)
    	elif val <= 1013 and val >= 1005:
		print ("1 egg",val)
		#if (check == 0):
		#	check = 1
		#	sendDataEGG(1)
		#elif (check == 1):
		#	check = 1
		#else:
                #        check = 1
                #        sendDataEGG(1)
		sendDataDRINK(1)
    	elif val <= 1004 and val >= 992:
        	print ("2 egg",val)
		#if (check == 1):
                #        check = 2
                #        sendDataEGG(2)
                #elif (check == 2):
                #        check = 2
		#else:
		#	check = 2
		#	sendDataEGG(2)
		sendDataDRINK(2)
	elif val <= 991 and val >= 984:
               print ("3 egg",val)
               #if (check == 2):
               #         check = 3
               #         sendDataEGG(3)
               #elif (check == 3):
               #         check = 3
	       #else:
	       #         check = 3
	       #	 sendDataEGG(3)
	       sendDataDRINK(3)
	elif val <= 983 and val >= 976:
                print ("4 egg",val)

                #if (check == 3):
                #        check = 4
                #        sendDataEGG(4)
                #elif (check == 4):
                #        check = 4
                #else:
                #        check = 4
                #        sendDataEGG(4)
		#	url = 'http://localhost:3000/setupEgg'
		#	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
		#	response = requests.get(url,headers=headers)
		sendDataDRINK(4)
	elif val <= 975 and val >= 966:
                print ("5 egg",val)

                #if (check == 4):
                #        check = 5
                 #       sendDataEGG(5)
                #elif (check == 5):
                #        check = 5
                #else:
                 #       check = 5
                  #      sendDataEGG(5)
		sendDataDRINK(5)
	elif val <= 965 and val >= 954:
                print ("6 egg",val)

                #if (check == 5):
                 #       check = 6
                  #      sendDataEGG(6)
                #elif (check == 6):
                 #       check = 6
                #else:
                 #       check = 6
                  #      sendDataEGG(6)
		sendDataDRINK(6)
	elif val <= 953 and val >= 948:
                print ("7 egg",val)

                #if (check == 6):
                 #       check = 7
                  #      sendDataEGG(7)
                #elif (check == 7):
                 #       check = 7
                #else:
                 #       check = 7
                  #      sendDataEGG(7)
		sendDataDRINK(7)
	elif val <= 947 and val >= 940:
                print ("8 egg",val)

                #if (check == 7):
                 #       check = 8
                  #      sendDataEGG(8)
                #elif (check == 8):
                 #       check = 8
                #else:
                 #       check = 8
                  #      sendDataEGG(8)
		sendDataDRINK(8)
	elif val <= 939 and val >= 930:
                print ("9 drink",val)

                #if (check == 8):
                 #       check = 9
                  #      sendDataEGG(9)
                #elif (check == 9):
                 #       check = 9
                #else:
                 #       check = 9
                  #      sendDataEGG(9)
		sendDataDRINK(9)
