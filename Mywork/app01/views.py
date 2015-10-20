from django.shortcuts import render, render_to_response
from django.template.context_processors import request
from django.http.response import HttpResponse
from app01.models import User
import json

# Create your views here.

name=""

def Index(request):
    
    return render_to_response('index.html',{'username':name})

def Login(request):
    
    return render_to_response('login.html')

def Auth(request):
    try:
        global name
        name = request.GET['username']
        passwd = request.GET['password']
        user = User.objects.get(name=name,password=passwd)
        return render_to_response('index.html',{'username':user})
    except Exception,e:
#         data={'error':'username or password wrong!'}
        return  HttpResponse("<h1 align ='center'>404 Not found</h1>")
    
def Menu(request):
#     user=request.GET['val']
    region_dic={
            'lizhaoning':{'age':20,'grade':100},
            'huangtao':{'age':20,'grade':99}
                }
    return HttpResponse(json.dumps(region_dic))
