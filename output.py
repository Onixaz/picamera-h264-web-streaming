from io import BytesIO
from threading import Condition

class StreamingOutput(object):
    def __init__(self):
        self.frame = None
        self.buffer = BytesIO()
        self.condition = Condition()
        self.separator = b'\x00\x00\x00\x01'
        
        

    def write(self, buf):
        if buf.startswith(self.separator):           
            self.buffer.seek(0)
            with self.condition:
                self.frame = self.buffer.read()
                self.condition.notify_all()   
            self.buffer.seek(0)
            self.buffer.truncate() 
        return self.buffer.write(buf)