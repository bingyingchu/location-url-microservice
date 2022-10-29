import time
import zmq
import urllib.parse
"""
A location url microservice
param name of the location: String
return url of the location on Google Maps: String
"""

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    # receive name of the location
    name = socket.recv().decode("utf-8")

    time.sleep(1)

    # compose the url by encoding space characters to plus sign (+)
    location = urllib.parse.quote_plus(name)
    url = "https://www.google.com/maps/search/%s/" % location

    # send back the url
    socket.send_string(url)

