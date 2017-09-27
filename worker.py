#!/usr/bin/env python

import threading
import json
import utils


#This is what gets spawned by the server when it receives a connection.
class Worker(threading.Thread):
    def __init__(self, sock, address):
        threading.Thread.__init__(self)
        self.sock = sock
        self.address = address

    def run(self):
        utils.log_stdout("worker %s has started." % threading.current_thread().getName())
        
        data = self.sock.recv(1024)
        utils.log_stdout("received data from device %s:  [%s]" % (self.address[0], data))

        response = {"success": 200, "msg": "This note is from worker %s on the server!" % threading.current_thread().getName()}

        self.sock.send(json.dumps(response))

        self.sock.close()
