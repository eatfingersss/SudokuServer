import zmq
import engine
import log

def listen(port):
    print("Game start at" + port)
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("udp://*:" + port)

    while True:
        message = socket.recv()
        
