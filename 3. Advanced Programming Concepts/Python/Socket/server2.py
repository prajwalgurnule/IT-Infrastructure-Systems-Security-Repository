import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 1234))
s.listen()

print("Chat server waiting for the client")
conn , addr = s.accept()
print("Connected to - ", addr)
while True:
    message = conn.recv(1026).decode()
    if not message or message == "bye":
        print("Client ended the chat")
        break
    print("Client : ",message)
    reply = input("server reply : ")
    conn.send(reply.encode())
    if reply == "bye":
        break

conn.close()
s.close()
print("Server disconnecting")