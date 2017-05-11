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

def sendDataEGG(data):
	print ("Sending..... ",data)
	url = 'http://localhost:3000/dataEgg'
       	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
	payload = {'egg': data}
        response = requests.post(url,data=payload)

check = -1


while True:

    	val = analogRead(ldr_channel)
	time.sleep(0.5)


    	if val > 1020:
		print ("No",val)
		if (check == 1):
			check = 0
			sendDataEGG(0)
		elif (check == 0):
			check = 0
		elif (check == -1):
			check = 0
			sendDataEGG(0)

    	elif val <= 1020 and val >= 1001:
		print ("1 egg",val)
		if (check == 0):
			check = 1
			sendDataEGG(1)
		elif (check == 1):
			check = 1
		else:
                        check = 1
                        sendDataEGG(1)

    	elif val <= 1000 and val >= 981:
        	print ("2 egg",val)
		if (check == 1):
                        check = 2
                        sendDataEGG(2)
                elif (check == 2):
                        check = 2
		else:
			check = 2
			sendDataEGG(2)

	elif val <= 980 and val >= 961:
               print ("3 egg",val)
               if (check == 2):
                        check = 3
                        sendDataEGG(3)
               elif (check == 3):
                        check = 3
	       else:
			check = 3
			sendDataEGG(3)

	elif val <= 960 and val >= 941:
                print ("4 egg",val)

                if (check == 3):
                        check = 4
                        sendDataEGG(4)
                elif (check == 4):
                        check = 4
                else:
                        check = 4
                        sendDataEGG(4)
			url = 'http://localhost:3000/setupEgg'
			headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
			response = requests.get(url,headers=headers)

	elif val <= 940 and val >= 921:
                print ("5 egg",val)

                if (check == 4):
                        check = 5
                        sendDataEGG(5)
                elif (check == 5):
                        check = 5
                else:
                        check = 5
                        sendDataEGG(5)

	elif val <= 920 and val >= 901:
                print ("6 egg",val)

                if (check == 5):
                        check = 6
                        sendDataEGG(6)
                elif (check == 6):
                        check = 6
                else:
                        check = 6
                        sendDataEGG(6)

	elif val <= 900 and val >= 881:
                print ("7 egg",val)

                if (check == 6):
                        check = 7
                        sendDataEGG(7)
                elif (check == 7):
                        check = 7
                else:
                        check = 7
                        sendDataEGG(7)

	elif val <= 880 and val >= 861:
                print ("8 egg",val)

                if (check == 7):
                        check = 8
                        sendDataEGG(8)
                elif (check == 8):
                        check = 8
                else:
                        check = 8
                        sendDataEGG(8)

	elif val <= 860 and val >= 841:
                print ("9 egg",val)

                if (check == 8):
                        check = 9
                        sendDataEGG(9)
                elif (check == 9):
                        check = 9
                else:
                        check = 9
                        sendDataEGG(9)

	elif val <= 840 and val >= 821:
                print ("10 egg",val)

                if (check == 9):
                        check = 10
                        sendDataEGG(10)
                elif (check == 10):
                        check = 10
