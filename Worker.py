import threading
import time

#this is what gets spawned by the web server when it receives a connection

class worker(threading.Thread):
    def __init__(self, sock):
        threading.Thread.__init__(self)
        self.sock = sock

    def run(self):
        #get i/o streams

        print "worker thread has started"
        print threading.current_thread()
        
        data = self.sock.recv(1024)
        print "received [%s]" % data

        self.sock.send("this note is from the worker thread (%s) on the server!" % threading.current_thread())
        time.sleep(600)

        self.sock.close()