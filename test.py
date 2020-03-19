import paho.mqtt.client as mqtt #import the client1
import time
from astral import LocationInfo
from astral.sun import sun
from pytz import *
import datetime
############
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

def on_log(client, userdata, level, buf):
	print("log: ",buf)

#  Dit pythyon prg drukt de huidige tijd af
#  de zonsopkomst en ondergang
#  voor een vaste locatie
#
#  Gerard Doets
#  18 maart 2020
#  Naam : zonOpkomstEnOndergang.py

from astral import LocationInfo
from astral.sun import sun
from pytz import *
import datetime

def zon(opofonder):

	city = LocationInfo()
	city.region = "Netherlands"

	###voor nijverdal
	city.name      = "Nijverdal"
	city.latitude  = 52.366146
	city.longitude = 6.443098

	###Voor Meppel
	city.name      = "Meppel"
	city.latitude  = 52.701499
	city.longitude = 6.232482

	tijdzoneAmsterdam = timezone("Europe/Amsterdam")
	nu                = datetime.datetime.now()
	city.timezone     = tijdzoneAmsterdam

#	print ("Huidige tijd : ")
#	print (nu.strftime("%Y-%m-%d %H:%M:%S"))
	s = sun(city.observer, date=nu ,tzinfo=tijdzoneAmsterdam )

#	print(city.name)
#	print(city.latitude)
#	print(city.longitude)
#	print('Zon')
	
	if opofonder == "onder":
#		print((f'ondergang: {s["sunset"]}\n'))	
		return((f'ondergang: {s["sunset"]}\n'))	
#		return s["sunrise"]
#		return "1846"

	if opofonder == "op":
		print((f'opkomst  : {s["sunrise"]}\n'))
		return s["sunset"]



########################################

#broker_address="192.168.1.184"
tijd = zon("onder")
broker_address="broker.hivemq.com"
print("creating new instance")
client = mqtt.Client("P3") #create new instance
#client.on_log=on_log
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker

client.loop_start() #start the loop
print("Subscribing to topic","house/bulbs/bulb1")
client.subscribe("house/bulbs/bulb1")
print("Publishing message to topic","house/bulbs/bulb1")

#client.publish("zonopofonder",tijd)
client.publish("house/bulbs/bulb1",tijd)
time.sleep(4) # wait
client.loop_stop() #stop the loop
