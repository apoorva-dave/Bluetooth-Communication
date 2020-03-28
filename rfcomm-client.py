import bluetooth

bd_addr = "" # bluetooth address of server to which u want to connect

port = 3

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr,port))
print("Send data to server. Start typing. Bye is for quitting.")
while 1:
	text = input()
	if text == "bye":
		break
	else:
		sock.send(text)
		print(sock.recv(1024))

sock.close()
