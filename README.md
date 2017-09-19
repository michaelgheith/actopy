# actopy
This is a multithreaded python bluetooth server.  To be used with the actopy client.  Inspired and created on the Raspberry Pi 3.  Created by Michael Gheith @ Juxtaploitation.

https://github.com/michaelgheith/actopy

* Email:  michael@juxtaploitation.com
* Website:  https://www.juxtaploitation.com/


## About
This provides a basic framework for you to have multiple bluetooth clients served by a single server instance; similiar to an HTTP server.  Usage is up to your imagination, be creative!  The server will broadcast a service name, along with a uuid.  The clients will look for this service, and will try to establish a connection to the server.  The server machine must be in [discoverable mode](#discoverable-mode) for this to work, and the bluetooth daemon needs to be run in [compatibility mode](#compatibility-mode).

## Dependencies
You will need to install pybluez so we can import bluetooth:<br/>
https://github.com/karulis/pybluez

## Discoverable Mode
This is a CLI tool for you to control your bluetooth device.  Do the following to make your device discoverable manually:
$ bluetoothctl<br/>
[bluetooth]# help<br/>
[bluetooth]# discoverable yes<br/>
[bluetooth]# quit<br/>

Or

$ sudo hciconfig hci0 piscan

Or if you want to have your device always in discoverable mode and not timeout after so many seconds we can modify the main bluetooth configuration file:<br/>
vim /etc/bluetooth/main.conf  
and then make sure you have the following set:<br/>
DiscoverableTimeout = 0

## Compatibility Mode
In order for the pybluez library to work on the Raspberry Pi, you need to do the following:<br/>
sudo vim /lib/systemd/system/bluetooth.service<br/>
Now add --compat to the ExecStart line like the following:<br/>
ExecStart=/usr/lib/bluetooth/bluetoothd --compat

## Random
To check the status of your bluetooth device:<br/>
$ systemctl status bluetooth

To get the MAC address of your device:<br/>
$ bluetoothctl list 

## Resources
* http://people.csail.mit.edu/rudolph/Teaching/Articles/PartOfBTBook.pdf
* https://people.csail.mit.edu/albert/bluez-intro/index.html
* https://github.com/karulis/pybluez/blob/master/examples/simple/sdp-browse.py
* https://learn.adafruit.com/install-bluez-on-the-raspberry-pi/installation
