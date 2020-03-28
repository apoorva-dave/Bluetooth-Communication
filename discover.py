import bluetooth

nearby_devices = bluetooth.discover_devices()

for bd_addr in nearby_devices:
	print(bd_addr)
	print(bluetooth.lookup_name(bd_addr))