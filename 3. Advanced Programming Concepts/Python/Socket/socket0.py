import socket
s = socket.socket()
print("Socket created")
s.bind(('localhost',8081))
s.listen(3)
print("Waiting for the connection")
while True:
   c, addr = s.accept()
   name = c.recv(1024).decode()
   print("Connection with", addr, name)
   c.send(bytes('Welcome to Connection','utf-8'))
   c.close()