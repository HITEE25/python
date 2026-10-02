import socket

c = socket.socket()
c.connect(("localhost",1234))

while True:
    msg = input("Client: ")
    c.send(msg.encode())

    print("Server: ",c.recv(1024).decode())
    if msg.lower() == "bye":
        break

c.close()
