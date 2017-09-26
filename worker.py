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
        utils.log_stdout("worker %s has started." % threading.current_thread().getName())
        
        data = self.sock.recv(1024)
        utils.log_stdout("received [%s]" % data)

        self.sock.send("This note is from worker %s on the server!" % threading.current_thread().getName())

        self.sock.close()
