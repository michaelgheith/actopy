import bluetooth
import Worker
import sys

class Server():
    def __init__(self):
        self.q_len = 5
        self.port = bluetooth.PORT_ANY
        self.server_sock = None

    def start_server(self):
        self.server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.server_sock.bind(("", self.port))
        self.server_sock.listen(self.q_len)  #Queue up as many as 5 connect requests.
        print "listening on port %d" % self.port

    def advertise_service(self, name, uuid):
        bluetooth.advertise_service(self.server_sock, name, uuid)

    def accept_connections(self):
        while True:
            client_sock, address = self.server_sock.accept()
            print "Accepted connection from %s" % address
            Worker.worker(client_sock).start()  #Spawns the worker thread.

    def run(self):
        self.start_server()
        self.advertise_service(name="FooBar Service", uuid="1e0ca4ea-299d-4335-93eb-27fcfe7fa848")
        self.accept_connections()

    def kill(self): 
        self.server_sock.close()
        sys.exit()


if __name__ == "__main__":
    multithreaded_server = Server()
    multithreaded_server.run()
    #multithreaded_server.kill()