#!/usr/bin/python3
# dit prg leest arduino uit 
# stoord de waarden in de db
# als de zon nog niet onder is abort de uitvoering
# voor test wijzig de waarde in de functie test() in myLib
# Gerard Doets gerarddoets@GMAIL.COM
# 23 maart 2020
#import paho.mqtt.client as mqtt 
import serial
import datetime
import time
from influxdb   import InfluxDBClient
from astral     import LocationInfo
from astral.sun import sun
from pytz       import *
from myLib      import *

#############################################
def storeInDB(paramOmgevingsTemperatuur, paramIRTemperatuur):
	nu = datetime.datetime.now()
	json_body = [
		{	"measurement": "irMeting2","tags": {"tijdstip": nu },
			"fields": {
				"omgevingsTemperatuur": paramOmgevingsTemperatuur,
				"IRTemp"              : paramIRTemperatuur}
		}
	]
	client.write_points(json_body)

#############################################
################### start ###################
if zonOnder() or test():
	client  = InfluxDBClient(host='localhost', port=8086)
	meetwaardeOmgevingsTemperatuur = 0
	meetwaardeIRTemperatuur        = 0

	client.switch_database('pyexample')
	ser = serial.Serial('/dev/ttyUSB0', 9600)
	time.sleep(10)
	teller    = 0
	maxTeller = 500
	while teller < maxTeller and (zonOnder() or test()):
		teller+=1
		if test():
			print(teller)
		time.sleep(10)
		binDataregel = ser.readline()
		dataregel    = binDataregel.decode('utf-8')
		lijst        = dataregel.split(';',3)
		aantal = 0
		for element in lijst:
			aantal = aantal +1
		if aantal == 3 :
			try:
				omgevingstemp = gdStrip(lijst[0])
				irtemp        = int(lijst[1])
				delta         = gdStrip(lijst[2])
				if irtemp - omgevingstemp == delta :
					storeInDB(omgevingstemp,irtemp) 
			except ValueError as e:
				print("ValueError")
				print(lijst)
				print("Teller = %d" %(teller))


