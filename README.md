# Bluetooth-Communication
Communicating with RFCOMM using python

Sample application to show how bluetooth feature can be used for communication using python

## Dependencies

1. Python 3
2. PyBluez - Bluetooth Python extension module. Use `pip install PyBluez` to install

That's it! 

## Setup

There are 3 files in this repository -
1. discover.py - discovers nearby bluetooth devices
2. rfcomm-server.py - server side connection file
3. rfcomm-client.py - client side connection file

## How to run?

I used two laptops. 1 windows laptop to make server and 1 mac laptop to make client.

Run rfcomm-server.py on windows laptop

![Capture](https://user-images.githubusercontent.com/19779081/77830866-97207d80-7151-11ea-8f62-b9629ecd2dfb.png)

Run rfcomm-client.py on mac laptop

![WhatsApp Image 2020-03-29 at 12 05 12 AM](https://user-images.githubusercontent.com/19779081/77830885-b4554c00-7151-11ea-835d-fe9c1d81c195.jpeg)

## References

https://people.csail.mit.edu/albert/bluez-intro/

