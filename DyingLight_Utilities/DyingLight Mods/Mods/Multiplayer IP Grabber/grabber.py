import requests
import json

from scapy.all import *
from ip2geotools.databases.noncommercial import DbIpCity

def pc(packet):
    if packet.proto == 17:
        udp = packet.payload

while True:
    x = sniff(filter="udp and port 7777", prn=pc, store=1, count=1) # Dying Light UDP default Port is 7777
    y = x[0][IP].src
    z = x[0][IP].dst
 
    if z == "192.168.31.6": # Replace with your local IP
        pass
    else:
        try:
            print(f"Destination: IP Address: [{z}] Country: [{DbIpCity.get(z, api_key='free').country}] Region: [{DbIpCity.get(z, api_key='free').region}] City: [{DbIpCity.get(z, api_key='free').city}]")
        except:
            print(f"Destination: IP Address: [{z}] Country: [{DbIpCity.get(z, api_key='free').country}]")
