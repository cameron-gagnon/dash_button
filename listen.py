#!/usr/bin/env python3.5

from scapy.all import *
import requests

SERVER = "127.0.0.1"
PORT = "80"
URL = "http://{server}.{port}/signal/toggle".format(server=SERVER,port=PORT)

def toggle_lights():
    """
        send a request to the server running on the Pi to toggle the lights
        on/off
    """
    print("Sending request to {url}".format(url=URL))
    requests.get(URL)

def arp_display(pkt):
    if pkt[ARP].op == 1: # who-has (request)
        if pkt[ARP].hwsrc == '34:d2:70:4f:d2:ba': # my dash button's mac addr
            toggle_lights()

print(sniff(prn=arp_display, filter="arp", store=0))
