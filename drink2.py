import spidev
import time
import requests

analog_ch = 1

spi =spidev.SpiDev()
spi.open(0,0)

def readADC(adcnum):
	if adcnum > 7 or adcnum < 0:
		return -1
	r =spi.xfer2([4 | 2 | (adcnum >> 2), (adcnum & 3) << 6, 0])
	adcout = ((r[1] & 15) << 8) + r[2]
	return adcout

def sendDataDRINK(data):
        print ("Sending..... ",data)
        url = 'http://localhost:3000/dataDrink'
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        payload = {'drink': data}
        response = requests.post(url,data=payload)

check = -1

while True:
	val = readADC(analog_ch)
	time.sleep(0.3)

	if val >= 4068:
                print ("No",val)
                if (check == 1):
                        check = 0
                        sendDataDRINK(0)
                elif (check == 0):
                        check = 0
                elif (check == -1):
                        check = 0
                        sendDataDRINK(0)

        elif val <= 4067 and val >= 4058:
		print ("1 ",val)
                if (check == 0):
                        check = 1
                        sendDataDRINK(1)
                elif (check == 1):
                        check = 1
                else:
                        check = 1
                        sendDataDRINK(1)

	elif val <= 4057 and val >= 4048:
                print ("2 ",val)
                if (check == 1):
                        check = 2
                        sendDataDRINK(2)
                elif (check == 2):
                        check = 2
                else:
                        check = 2
                        sendDataDRINK(2)
			url = 'http://localhost:3000/setupDrink'
			headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
			response = requests.get(url,headers=headers)

	elif val <= 4037 and val >= 4028:
               	print ("3 ",val)
               	if (check == 2):
                        check = 3
                        sendDataDRINK(3)
               	elif (check == 3):
                        check = 3
               	else:
                        check = 3
                        sendDataDRINK(3)

        elif val <= 4017 and val >= 4008:
                print ("4 ",val)

                if (check == 3):
                        check = 4
                        sendDataDRINK(4)
                elif (check == 4):
                        check = 4
                else:
                        check = 4
                        sendDataDRINK(4)

	elif val <= 3997 and val >= 3988:
                print ("5 ",val)

                if (check == 4):
                        check = 5
                        sendDataDRINK(5)
                elif (check == 5):
                        check = 5
                else:
                        check = 5
                        sendDataDRINK(5)

	elif val <= 3967 and val >= 3958:
                print ("6 ",val)

                if (check == 5):
                        check = 6
                        sendDataDRINK(6)
                elif (check == 6):
                        check = 6
                else:
                        check = 6
                        sendDataDRINK(6)

        elif val <= 3940 and val >= 3921:
                print ("7 ",val)

                if (check == 6):
                        check = 7
                        sendDataDRINK(7)
                elif (check == 7):
                        check = 7
                else:
                        check = 7
                        sendDataDRINK(7)

	elif val <= 3920 and val >= 3901:
                print ("8 ",val)

                if (check == 7):
                        check = 8
                        sendDataDRINK(8)
                elif (check == 8):
                        check = 8
                else:
                        check = 8
                        sendDataDRINK(8)

	elif val <= 3900 and val >= 3881:
                print ("9 ",val)

                if (check == 8):
                        check = 9
                        sendDataDRINK(9)
                elif (check == 9):
                        check = 9
                else:
                        check = 9
                        sendDataDRINK(9)

        elif val <= 3880 and val >= 3861:
                print ("10 ",val)

                if (check == 9):
                        check = 10
                        sendDataDRINK(10)
                elif (check == 10):
                        check = 10
		else:
                        check = 10
                        sendDataDRINK(10)

	elif val <= 3860 and val >= 3841:
                print ("11 ",val)

                if (check == 10):
                        check = 11
                        sendDataDRINK(11)
                elif (check == 11):
                        check = 11
                else:
                        check = 11
                        sendDataDRINK(11)

	elif val <= 3840 and val >= 3821:
                print ("12 ",val)

                if (check == 11):
                        check = 12
                        sendDataDRINK(12)
                elif (check == 12):
                        check = 12
