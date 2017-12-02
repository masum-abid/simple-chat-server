import socket

HOST = '192.168.0.103'
PORT = 8000
s = socket.socket()
s.connect((HOST, PORT)) # client-side, connects to a host
while True:
	message = input("Your Message: ") 
	s.send(message.encode()) 
	print ("Awaiting reply")
	reply = s.recv(1024) # 1024 is max data that can be received 
	print ("Received ", repr(reply.decode()))

s.close()
