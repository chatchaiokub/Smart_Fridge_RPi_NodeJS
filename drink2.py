import spidev
import time 

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

CHECK = -1

while True:
	value = readADC(analog_ch)
	print("analog_ch1=",value)
	time.sleep(0.3)
	
	if val >= 1006:
                print ("No",val)
                if (check == 1):
                        check = 0
                        sendDataEGG(0)
                elif (check == 0):
                        check = 0
                elif (check == -1):
                        check = 0
                        sendDataEGG(0)

        elif val < 1005 and val >= 980:
		print ("1 egg",val)
                if (check == 0):
                        check = 1
                        sendDataEGG(1)
                elif (check == 1):
                        check = 1
                else:
                        check = 1
                        sendDataEGG(1)

	elif val <= 979 and val >= 955:
                print ("2 egg",val)
                if (check == 1):
                        check = 2
                        sendDataEGG(2)
                elif (check == 2):
                        check = 2
                else:
                        check = 2
                        sendDataEGG(2)
	
	elif val <= 954 and val >= 935:
               	print ("3 egg",val)
               	if (check == 2):
                        check = 3
                        sendDataEGG(3)
               	elif (check == 3):
                        check = 3
               	else:
                        check = 3
                        sendDataEGG(3)

        elif val <= 979 and val >= 955:
                print ("4 egg",val)

                if (check == 3):
                        check = 4
                        sendDataEGG(4)
                elif (check == 4):
                        check = 4
                else:
                        check = 4
                        sendDataEGG(4)
             
	elif val <= 979 and val >= 955:
                print ("5 egg",val)

                if (check == 4):
                        check = 5
                        sendDataEGG(5)
                elif (check == 5):
                        check = 5
                else:
                        check = 5
                        sendDataEGG(5)

	elif val <= 979 and val >= 955:
                print ("6 egg",val)

                if (check == 5):
                        check = 6
                        sendDataEGG(6)
                elif (check == 6):
                        check = 6
                else:
                        check = 6
                        sendDataEGG(6)

        elif val <= 979 and val >= 955:
                print ("7 egg",val)

                if (check == 6):
                        check = 7
                        sendDataEGG(7)
                elif (check == 7):
                        check = 7
                else:
                        check = 7
                        sendDataEGG(7)

	elif val <= 979 and val >= 955:
                print ("8 egg",val)

                if (check == 7):
                        check = 8
                        sendDataEGG(8)
                elif (check == 8):
                        check = 8
                else:
                        check = 8
                        sendDataEGG(8)

	elif val <= 979 and val >= 955:
                print ("9 egg",val)

                if (check == 8):
                        check = 9
                        sendDataEGG(9)
                elif (check == 9):
                        check = 9
                else:
                        check = 9
                        sendDataEGG(9)

        elif val <= 979 and val >= 955:
                print ("10 egg",val)

                if (check == 9):
                        check = 10
                        sendDataEGG(10)
                elif (check == 10):
                        check = 10
		else:
                        check = 10
                        sendDataEGG(10)
	
	elif val <= 979 and val >= 955:
                print ("11 ",val)

                if (check == 10):
                        check = 11
                        sendDataDRINK(11)
                elif (check == 11):
                        check = 11
                else:
                        check = 11
                        sendDataDRINK(11)

	elif val <= 979 and val >= 955:
                print ("12 ",val)

                if (check == 11):
                        check = 12
                        sendDataDRINK(12)
                elif (check == 12):
                        check = 12
             
