#!/usr/bin/python3
import datetime
from astral import LocationInfo
from astral.sun import sun
from pytz import *

#############################################
def test():
# hier zet je of je wilt testen bij daglicht of 
# runnen in real life
	return (False)   #   real life
###	return (True) #   testen bij daglicht

#############################################
def zon(opofonder):
	city = LocationInfo()
	city.region = "Netherlands"

	###voor nijverdal
	city.name      = "Nijverdal"
	city.latitude  = 52.366146
	city.longitude = 6.443098

	###Voor Meppel
	if test(): 	
		city.name         = "Meppel"
		city.latitude     = 52.701499
		city.longitude    = 6.232482

	tijdzoneAmsterdam = timezone("Europe/Amsterdam")
	nu                = datetime.datetime.now()
	if test(): 	
		print(nu)
	city.timezone     = tijdzoneAmsterdam

	s = sun(city.observer, date=nu ,tzinfo=tijdzoneAmsterdam )
	if test(): 	
		for k in ["dawn", "sunrise", "noon", "sunset", "dusk"]:
			print( "%7s %s" % (k, s[k]))

	if opofonder == "onder":
		return(s["sunset"])	
	if opofonder == "op":
		return(s["sunrise"])

#############################################
def zonOnder():
	nu    = datetime.datetime.timestamp(datetime.datetime.now())
	onder = datetime.datetime.timestamp(zon("onder"))
	if nu  > onder :
		return(True)
	else:
		return(False)

#############################################
def zonOp():
	nu = datetime.datetime.timestamp(datetime.datetime.now())
	op = datetime.datetime.timestamp(zon("op"))
	if op < nu :
		return(True)
	else:
		return(False)

#############################################
def huidigeUur():
	hhmm = datetime.datetime.now().time()
	strhhmm = str(hhmm)
	regel   = strhhmm.split(':',3)
	return regel[0]

#############################################
def gdStrip(erin):
	erin = erin.strip()
	eruit = ""
	for c in erin:
		asciiwaarde = ord(c)
		if asciiwaarde >= 48 and   asciiwaarde <= 57 or asciiwaarde == 45 :
			eruit = eruit + c 
	return int(eruit)


		
