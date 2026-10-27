import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
alert = [
    "112: NAtional Emergency",
    "100: Police",
    "108: Ambulance"
]
r = ("localhost",1234)
for a in alert:
    s.sendto(
        a.encode(), r
    )
    print("Sent : ",alert)
s.close()