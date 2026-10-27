import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c.connect(("localhost", 1234))
message = input("Enter the message : ")
c.send(message.encode())
response = c.recv(1024).decode()
print("Modified Message - ")
print(response)
c.close()