import socket
r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
r.bind(("localhost",1234))
print("emergency alert recver is listening")
for i in range(3):
    data, addr = r.recvfrom(1024)
    alert = data.decode()
    print("Alert : ",alert)
    print("Sender address : ",addr)
    print()
r.close()