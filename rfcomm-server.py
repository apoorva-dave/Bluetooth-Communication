import bluetooth

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
print("Socket successfully created")
port = 3
server_sock.bind(("",port))
print("Binding done")
print("server's address")
print(server_sock.getsockname())

print("Socket binded to %s" %(port))
server_sock.listen(1)

try:
	client_sock, address = server_sock.accept()
	print("Accepted connection from address", address)
	while 1:
		data = client_sock.recv(1024)
		if data:
			print("Received [%s]"%data)
			client_sock.send("Thanks for connecting. Data received")
		else:
			print("Client says bye!")
			break
except:
    print("Closing socket")
    client_sock.close()
    server_sock.close()