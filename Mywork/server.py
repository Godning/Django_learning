# -*- coding:utf-8 -*-
'''
Created on 2015��8��23��

@author: luke
'''
import socket, os

host = 'localhost'
port = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

while 1:
    conn, addr = s.accept()
    print 'Connected by', addr
    while 1:
        data = conn.recv(1024)
        if not data:
            break
        print 'Command by', addr, data
        cmd_result = os.popen(data).read()
        conn.sendall(cmd_result)
conn.close()
