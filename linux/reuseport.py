import socket
import os
#xiaorui.cc
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
s.bind(('0.0.0.0', 1234))
s.listen(1)

while True:
    conn, addr = s.accept()
    print('Connected to {}'.format(os.getpid()))
    data = conn.recv(1024)
    conn.send(data)
    conn.close()
