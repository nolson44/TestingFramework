#!/usr/bin/env python
# Echo client program
import socket

HOST = ''    		  # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
file1 = open('test.txt','r')
content = file1.read()
s.send(content)
data = s.recv(1024)
s.close()
file1.close()
print 'Received', data
