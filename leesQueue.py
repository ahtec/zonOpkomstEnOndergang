#!/usr/bin/python3

import paho.mqtt.subscribe as subscribe 

#broker_address="192.168.1.184"
broker_address="broker.hivemq.com"
msg = subscribe.simple("zonopofonder", hostname=broker_address)
print("%s %s" % (msg.topic, msg.payload))

