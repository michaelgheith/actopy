#!/usr/bin/env python

import threading
import time


#This is what gets spawned by the server when it receives a connection.
class Worker(threading.Thread):
    def __init__(self, sock):
        threading.Thread.__init__(self)
        self.sock = sock

    def run(self):
        print "Worker thread %s has started." % threading.current_thread()
        
        data = self.sock.recv(1024)
        print "Received [%s]" % data

        self.sock.send("This note is from the worker thread %s on the server!" % threading.current_thread())

        self.sock.close()