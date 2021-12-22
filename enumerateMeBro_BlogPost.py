import socket
import time

# Set Up Variables
targetPort = 1313
targetIP = "127.0.1.1"
wordListRoot = "oneWordCommandList.txt"
wordListTarget = "oneWordTargetList.txt"

currentFormat = "utf-8"
targetAddress = (targetIP,targetPort)

# AF_INET is the family were using (v4 Addresses)
# SOCK_STREAM  will tell Python it's going to be a TCP socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# This is our initial connection/handshake
clientSocket.connect(targetAddress)

# Read the wordlist, get the word, send the message, move onto next word
def getCommandToSend(currentWordList):
	
	# Take the input value and read the file
	with open(currentWordList) as currentList:
		
		# Go line by line
		for line in currentList:
			sendMessage(line)

# Read the target wordlist, get the word, send the message, move onto next word
def getTargetToSend(command, currentWordList):
	
	# Take the input value and read the file
	with open(currentWordList) as currentList:
		
		# Go line by line
		for line in currentList:
			
			# Were going to construct the message as "command currentLine"
			line = command + " " + line
			sendMessage(line)

# Recieves the current list
def sendMessage(targetMessage):
	
	# take out input message and encode it with UTF-8
	currentMessage = targetMessage.encode(currentFormat)
	
	# print it so we can se the input
	print(targetMessage)
	
	#Send the message
	clientSocket.send(currentMessage)
	
	# Slow down the requests by 3 seconds
	time.sleep(3)
	
	# print the response if any, we use 2048 bytes to try to catch everything
	# we then decode the message back into a human readable format "utf-8"
	print(clientSocket.recv(2048).decode(currentFormat))
	
	

# uncomment what command you want to use. 

#getCommandToSend(wordListRoot)

# command I want to focus on
#targetCommand = "start"
#getTargetToSend(targetCommand,wordListTarget)
