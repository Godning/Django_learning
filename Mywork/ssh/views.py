from django.shortcuts import render, render_to_response
from django.template.context_processors import request
from django.http.response import HttpResponse
import socket
from ssh.models import CMD
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
    try:
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
        cmd_new=CMD(cmd=cmd,result=data)
        cmd_new.save()
        s.close()
        return HttpResponse(data)
    except Exception,e:
        return HttpResponse("Server is not connected!")

def log(request):
    try:
        cmd_result=CMD.objects.all()
        print cmd_result
        return render_to_response('show.html',{'result':cmd_result})
    except Exception,e:
        return render_to_response('show.html',{'result':str(e)})
