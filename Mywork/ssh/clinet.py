# -*- coding:gbk -*-
'''
@author: luke
'''
import socket

host = 'localhost'
port = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
while 1:
    cmd = raw_input("Your command:").strip()        
    if cmd == 0: 
        continue
    else:
        if cmd == 'q':break
        s.sendall(cmd + '\n')
    if cmd.split()[0] == 'get':
        with open(cmd.split()[1], 'wb') as f:
            while 1:
                data = s.recv(1024)
                if data == 'FileTransferDone':
                    break
                f.write(data)
        print 'Get Successful!'
        continue
    data = s.recv(1024)
    print u'Received', data          
s.close()
