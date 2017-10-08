#!/usr/bin/env python

import sys
import argparse
import bluetooth
import config
import worker
import utils


class Server():
    def __init__(self, name, uuid):
        self.q_len = 3
        self.port = bluetooth.PORT_ANY
        self.server_sock = None
        self.name = name
        self.uuid = uuid

    def start_server(self):
        self.server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.server_sock.bind(("", self.port))
        self.server_sock.listen(self.q_len)  #Queue up as many as 5 connect requests.
        utils.log_stdout("listening on port %d" % self.port)

    def advertise_service(self):
        bluetooth.advertise_service(self.server_sock, self.name, self.uuid)

    def accept_connections(self):
        while True:
            client_sock, address = self.server_sock.accept()
            utils.log_stdout("accepted connection from %s" % address[0])
            worker.Worker(client_sock, address).start()  #Spawns the worker thread.

    def run(self):
        self.start_server()
        self.advertise_service()
        self.accept_connections()

    def kill(self): 
        self.server_sock.close()
        sys.exit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="a multithreaded bluetooth server")
    parser.add_argument("-v", "--verbose", help="turn on verbose mode", action="store_true")
    parser.add_argument("-n", "--name", help="specify a service name", default="FooBar Service")
    parser.add_argument("-u", "--uuid", help="specify a uuid", default="1e0ca4ea-299d-4335-93eb-27fcfe7fa848")
    args = parser.parse_args()

    if args.verbose:
        config.logging = True
        utils.log_stdout("running {}".format(__file__))
        utils.log_stdout("verbose mode turned on")
        utils.log_stdout("using service name %s" % args.name)
        utils.log_stdout("using uuid %s" % args.uuid)

    try:
        multithreaded_server = Server(name=args.name, uuid=args.uuid)
        multithreaded_server.run()
    except KeyboardInterrupt:
        utils.log_stdout("shutting down the server")
        multithreaded_server.kill()
