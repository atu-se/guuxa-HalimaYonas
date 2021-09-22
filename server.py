import socket

s= socket.socket()
s.bind(('127.0.0.1',1027))

s.listen(3)

print("waiting connection")
while True:
            conn, addr = s.accept()
            data = conn.recv(127).decode()
            print("connected with",addr,data)

            conn.send(bytes('welcome to ATU','utf-8'))
            conn.close()