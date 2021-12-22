import socket
import threading
import time

portListenOn = 1313
serverIP = socket.gethostbyname(socket.gethostname())
protocolFormat = 'utf-8'

usedAddress = (serverIP,portListenOn)

# create our socket family and type
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(usedAddress)

def workClient(clientConnection, clientAdress):
	print("Connection from " + str(clientAdress))
	clientConnected = True
	while clientConnected:
		
		bodyMessage = clientConnection.recv(2048).decode(protocolFormat)
		print(str(clientAdress) + " " + bodyMessage)
		
		# Check for different commands
		if "pwd" in bodyMessage:
			clientConnection.send(b"/usr/var/iabm5000/")
			clientConnection.send(b"\n")

		if "ls" in bodyMessage:
				clientConnection.send(b"rawMaterialTracker.db \t\t scheduleShipping.txt")
				clientConnection.send(b"\ncontractAgreement.doc \t\t iabm5000.ini")
				clientConnection.send(b"\nbottleCapVendors.csv \t\t labelDesign.png")
				clientConnection.send(b"\nfactoryStartUp.sh \t\t cronBuilder.py")
				clientConnection.send(b"\n")
		
		# this will trigger some faulty logic
		# should be regexing user commands
		# never trust a user to enter a command correctly
		if "cat" in bodyMessage:
				
			if "cat /etc/passwd" in bodyMessage:
				clientConnection.send(b"Access Rejected")
				clientConnection.send(b"\n")
				
			elif "cat /etc/shadow" in bodyMessage:
				clientConnection.send(b"Access Rejected")
				clientConnection.send(b"\n")
					
			elif "cat bottleCapVendors.csv" in bodyMessage:
				clientConnection.send(b"coke,.00005,red,20mm\n")
				clientConnection.send(b"pepsi,.00005,blue,20mm\n")
				clientConnection.send(b"Jones,.00005,metallic gold,20mm\n")
				clientConnection.send(b"rc,.00010,red/blue,20mm\n")
				clientConnection.send(b"f1Oil,.0025,blcl,28mm\n")
				clientConnection.send(b"bawls,.1,metallic silver,20mm")
				clientConnection.send(b"\n")
			else:
				clientConnection.send(b"Rejected Request")
				clientConnection.send(b"\n")
		
				
		if "start" in bodyMessage:
			if "start bottle" in bodyMessage:
				clientConnection.send(b"Starting Bottling Process")
				clientConnection.send(b"\n")
			elif "start label" in bodyMessage:
				clientConnection.send(b"Starting Label Process")
				clientConnection.send(b"\n")
			elif "start cap" in bodyMessage:
				clientConnection.send(b"Starting Capping Process")
				clientConnection.send(b"\n")
				
			else:
				clientConnection.send(b"Please Include Start Process Target")
				clientConnection.send(b"\n")
				
		if "stop" in bodyMessage:
			if "stop bottle" in bodyMessage:
				clientConnection.send(b"Stopping Bottling Process")
				clientConnection.send(b"\n")
			elif "stop label" in bodyMessage:
				clientConnection.send(b"Stopping Label Process")
				clientConnection.send(b"\n")
			elif "stop cap" in bodyMessage:
				clientConnection.send(b"Stopping Capping Process")
				clientConnection.send(b"\n")
				
			else:
				clientConnection.send(b"Please Include Stop Process Target")
				clientConnection.send(b"\n")
		
		if "self-destruct" in bodyMessage:
			clientConnection.send(b"Starting Factory Self-Destruction Process in...")
			clientConnection.send(b"\n")
			time.sleep(2)
			clientConnection.send(b"5...")
			time.sleep(2)
			clientConnection.send(b"4...")
			time.sleep(2)
			clientConnection.send(b"3...")
			time.sleep(2)
			clientConnection.send(b"2...")
			time.sleep(2)
			clientConnection.send(b"1...")
			time.sleep(2)
			clientConnection.send(b"GoodBye")
			clientConnection.send(b"\n")
			break
						
		if "bye" in bodyMessage:
				clientConnection.send(b"Goodbye User")
				clientConnection.send(b"\n")
				break # Theres more elegant ways to do this but meh
		
		else:
			clientConnection.send(b"\n")
		
	# kill the current connection
	clientConnection.close()

def mainServerLoop():
	server.listen()
	print("ServerIP is: " + serverIP)
	while True:
		clientConnection, clientAdress = server.accept()
		thread = threading.Thread(target=workClient, args=(clientConnection, clientAdress))
		thread.start()
		
mainServerLoop()

