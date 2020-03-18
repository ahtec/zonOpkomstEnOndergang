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

print ("Huidige tijd : ")
print (nu.strftime("%Y-%m-%d %H:%M:%S"))
s = sun(city.observer, date=nu ,tzinfo=tijdzoneAmsterdam )

print(city.name)
print(city.latitude)
print(city.longitude)
print('Zon')
print((
    f'opkomst   : {s["sunrise"]}\n'
    f'ondergang : {s["sunset"]}\n'
))

