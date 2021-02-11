import zmq


class ZmqCon:
    context = None
    socket = None

    def __init__(self):
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind("tcp://*:")                          # apply free port

    def start(self, work):
        pass
        #while (True):
        #    work();
