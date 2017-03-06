#!/usr/bin/env python2.7

from scapy.all import *
from time import time
import requests

SERVER = "127.0.0.1"
PORT = "80"
URL = "http://{server}:{port}/signal/toggle".format(server=SERVER,port=PORT)
REQ_DELAY = 5 # delay 5 seconds in between requests. If the button sends 2 ARP's in
              # a short amount of time, we'll ignore them
last_request_time = 0

def toggle_lights():
    global last_request_time
    """
        send a request to the server running on the Pi to toggle the lights
        on/off
    """
    if (time() - last_request_time > REQ_DELAY):
        print "Sending request to {url}".format(url=URL)
        requests.get(URL)
        last_request_time = time()

def arp_display(pkt):
    if pkt[ARP].op == 1: # who-has (request)
        if pkt[ARP].hwsrc == '34:d2:70:4f:d2:ba': # my dash button's mac addr
            toggle_lights()

print sniff(prn=arp_display, filter="arp", store=0, count=0)
