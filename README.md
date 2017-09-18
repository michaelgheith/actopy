# actopy
This is a multithreaded python bluetooth server.  To be used with the actopy client.  Inspired and created on the Raspberry Pi 3.  Created by Michael Gheith @ Juxtaploitation.

[https://github.com/michaelgheith/actopy](https://github.com/michaelgheith/actopy)

Email:  michael@juxtaploitation.com
Website:  [https://www.juxtaploitation.com/](https://www.juxtaploitation.com/)


## About
This provides a basic framework for you to have multiple bluetooth clients served by a single server instance; similiar to an HTTP server.  Usage is up to your imagination, be creative!  The server will broadcast a service name, along with a uuid.  The clients will look for this service, and will try to establish a connection to the server.  The server machine must be in discoverable mode for this to work (see bluetoothctl section), and the bluetooth daemon needs to be run in compatibility mode (see Other section).

## Dependencies
You will need to install pybluez so we can import bluetooth.
https://github.com/karulis/pybluez

## bluetoothctl
This is a CLI for you to control your bluetooth device.  Do the following to make your device discoverable manually:
$ bluetoothctl
[bluetooth]# help
[bluetooth]# discoverable yes
[bluetooth]# quit

Or

sudo hciconfig hci0 piscan

Or if you want to have your device always in discoverable mode and not timeout after so many seconds we can modify the main bluetooth configuration file:
vim /etc/bluetooth/main.conf  
and then make sure you have the following set:
DiscoverableTimeout = 0

## Other
In order for this to work on the Raspberry Pi, you need to do the following:
sudo vim /lib/systemd/system/bluetooth.service
Now add --compat to the ExecStart line like the following:
ExecStart=/usr/lib/bluetooth/bluetoothd --compat

## Random
To check the status of your bluetooth device:
systemctl status bluetooth

To get the MAC address of your device:
bluetoothctl list 

## Resources
[http://people.csail.mit.edu/rudolph/Teaching/Articles/PartOfBTBook.pdf](http://people.csail.mit.edu/rudolph/Teaching/Articles/PartOfBTBook.pdf)
[https://people.csail.mit.edu/albert/bluez-intro/index.html](https://people.csail.mit.edu/albert/bluez-intro/index.html)
[https://github.com/karulis/pybluez/blob/master/examples/simple/sdp-browse.py](https://github.com/karulis/pybluez/blob/master/examples/simple/sdp-browse.py)
[https://learn.adafruit.com/install-bluez-on-the-raspberry-pi/installation](https://learn.adafruit.com/install-bluez-on-the-raspberry-pi/installation)