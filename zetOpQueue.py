#!/usr/bin/python3

import paho.mqtt.client as mqtt #import the client1
import time
from astral import LocationInfo
from astral.sun import sun
from pytz import *
import datetime

########################################
def on_log(client, userdata, level, buf):
	print("log: ",buf)
########################################
def zon(opofonder):
	city = LocationInfo()
	city.region = "Netherlands"

	###voor nijverdal
	city.name      = "Nijverdal"
	city.latitude  = 52.366146
	city.longitude = 6.443098

	###Voor Meppel
	city.name         = "Meppel"
	city.latitude     = 52.701499
	city.longitude    = 6.232482
	tijdzoneAmsterdam = timezone("Europe/Amsterdam")
	nu                = datetime.datetime.now()
	city.timezone     = tijdzoneAmsterdam

	s = sun(city.observer, date=nu ,tzinfo=tijdzoneAmsterdam )
	if opofonder == "onder":
		return(f'ondergang: {s["sunset"]}')	

	if opofonder == "op":
		return(f'opkomst  : {s["sunrise"]}')
########################################
def on_publish(client,userdata,result):            
    print("data published ")
    print(userdata)
    print(result)
    print("#######")
    pass
########################################

#broker_address="192.168.1.184"
tijd = zon("op")  # dit is een voorbeeld voor tijdstip zonsopgang
broker_address="broker.hivemq.com"
port=1883
client = mqtt.Client("SterrenwachtHellendoorn") 
client.on_publish = on_publish
client.on_log=on_log
client.connect(broker_address,port)
ret=client.publish("zonopofonder",tijd)
print("return waarde van publish")
print(ret)
