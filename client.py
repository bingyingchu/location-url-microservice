import zmq
import time

context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# send name of the location
socket.send(b"excelsior playground")

time.sleep(1)

# the url returned by the microservice
url = socket.recv().decode("utf-8")
print(url)
