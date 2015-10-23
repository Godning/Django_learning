from django.shortcuts import render, render_to_response
from django.template.context_processors import request
from django.http.response import HttpResponse
import socket
# Create your views here.
s=None

def SSH(request):
    return render_to_response('ssh.html')

def Connect(request):
    host = 'localhost'
    port = 50007
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return HttpResponse("success")

def SendCommand(request):
    host = 'localhost'
    port = 50007
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    cmd = request.POST.get('cmd')     
    if cmd: 
        if cmd == 'q':
            return HttpResponse("exit")
        s.sendall(cmd + '\n')   
    else:
        return HttpResponse("")
    print 'send success'
    data = s.recv(1024)
    print u'Received', data
    s.close()
    return HttpResponse(data)