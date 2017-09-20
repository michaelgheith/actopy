#!/usr/bin/env python

import sys
import argparse
import bluetooth
import worker


class Server():
    def __init__(self, name, uuid):
        self.q_len = 5
        self.port = bluetooth.PORT_ANY
        self.server_sock = None
        self.name = name
        self.uuid = uuid

    def start_server(self):
        self.server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.server_sock.bind(("", self.port))
        self.server_sock.listen(self.q_len)  #Queue up as many as 5 connect requests.
        print "listening on port %d" % self.port

    def advertise_service(self):
        bluetooth.advertise_service(self.server_sock, self.name, self.uuid)

    def accept_connections(self):
        while True:
            client_sock, address = self.server_sock.accept()
            print "Accepted connection from", address
            worker.Worker(client_sock).start()  #Spawns the worker thread.

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
        print "Verbose mode turned on."
        print "Running '{}'".format(__file__)
        print "using service name %s" % args.name
        print "using uuid %s" % args.uuid

    try:
        multithreaded_server = Server(name=args.name, uuid=args.uuid)
        multithreaded_server.run()
    except KeyboardInterrupt:
        print("\nShutting down the server.")
        multithreaded_server.kill()
