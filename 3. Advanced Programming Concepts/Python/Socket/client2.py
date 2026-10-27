import socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('localhost',1236))
while True:
    message = input("Client Message - ")
    c.send(message.encode())
    if message == "exit":
        break
    reply = c.recv(1024).decode()
    if not reply or reply == "exit":
        print("Server ended the chat")
        break;
    print("Server : ",reply)
c.close()
print("Client closed")