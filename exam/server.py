import socket

s = socket.socket()
s.bind(("localhost",1234))
s.listen(1)

c,addc = s.accept()

while True:
    print("client: ",c.recv(1024).decode())
    msg = input("Server: ")
    c.send(msg.encode())
    
    if msg.lower() == "bye":
        break

c.close()
s.close()