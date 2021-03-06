#!/usr/bin/env python

import threading
import json
import config
import utils


#This is what gets spawned by the server when it receives a connection.
class Worker(threading.Thread):
    def __init__(self, sock, address):
        threading.Thread.__init__(self)
        self.sock = sock
        self.address = address

    def run(self):
        if config.logging:
            utils.log_stdout("worker %s has started." % threading.current_thread().getName())
        
        data = self.sock.recv(1024)
        utils.log_stdout("received data from device %s on %s:  [%s]" % (self.address[0], threading.current_thread().getName(), data))

        response = {"status": 200, "msg": "This note is from worker %s on the server!" % threading.current_thread().getName()}

        try:
            self.sock.send(json.dumps(response))
        except Exception, e:
            utils.log_stderror(e)
        finally:
            self.sock.close()
