from socket import *


HOST = '192.168.0.103'
PORT = 8000
s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept() # accept the connection
print ('Connected by', addr) # print the address of the person connected
i = True
while i is True:
	data = conn.recv(1024) #recives datae (1024 bytes) using conn and store into data 
	print ("Received ", repr(data.decode())) # print data; Data is the message the users types
	reply = input("Reply: ") 
	conn.sendall(reply.encode())
conn.close()




conn.close()
