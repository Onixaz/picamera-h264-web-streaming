from threading import Thread

class BroadcastThread(Thread):
    def __init__(self, camera, output, websocket_server):
        super(BroadcastThread, self).__init__()
        self.camera = camera
        self.output = output
        self.websocket_server = websocket_server

    def run(self):
        try:
            self.camera.start_recording(self.output, 'h264', profile="baseline")
            while True:
                with self.output.condition:
                    self.output.condition.wait()
                    self.websocket_server.manager.broadcast(self.output.frame, binary=True)
                    
        except:
            raise Exception