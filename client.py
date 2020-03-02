import socket
tcp_ip = '94.142.241.111'
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((tcp_ip,23))

while True:
	msg = s.recv(500)
	print(msg.decode('ascii'))

 
