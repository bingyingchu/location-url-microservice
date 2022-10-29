This is a microservice developed for the Playdate web application. The communication pipe is ZeroMQ.

#### How to REQUEST data from the microservice:
The client needs to send a string of the location name to the microservice. Example:

```python
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# send name of the location
socket.send(b"excelsior playground")
```

#### How to RECEIVE data from the microservice:
The microservice receives the location name, parses the string by encoding space characters to plus sign (+) to compose the url, and sends back the url to the client.

#### Please see the following UML sequence diagram for a detailed demonstration:
![UML sequence diagram][diagram]
[diagram]: https://github.com/bingyingchu/location-url-microservice/SequenceDiagram.png