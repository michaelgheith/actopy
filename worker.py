#!/usr/bin/env python

import threading
import time
import utils


#This is what gets spawned by the server when it receives a connection.
class Worker(threading.Thread):
    def __init__(self, sock):
        threading.Thread.__init__(self)
        self.sock = sock

    def run(self):
        utils.log_stdout("worker thread %s has started." % threading.current_thread())
        
        data = self.sock.recv(1024)
        utils.log_stdout("received [%s]" % data)

        self.sock.send("This note is from the worker thread %s on the server!" % threading.current_thread())

        self.sock.close()
