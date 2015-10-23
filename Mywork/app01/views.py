from django.shortcuts import render, render_to_response
from django.template.context_processors import request
from django.http.response import HttpResponse
from django.core.files import File
from app01.models import User,UploadFiles
import json

# Create your views here.

name=""

def Index(request):
    
    return render_to_response('index.html',{'username':name})

def Login(request):
    
    return render_to_response('login.html')

def Auth(request):
    try:
        print request.POST
        global name
        name = request.POST.get('username')
        passwd = request.POST.get('password')
        print name,passwd
        user = User.objects.get(name=name,password=passwd)
        return render_to_response('index.html',{'username':user})
    except Exception,e:
#         data={'error':'username or password wrong!'}
        return  HttpResponse()
    
def uploadFile(request):
    if  (request.method == 'POST'):
        files = request.FILES.getlist('multipleFileUpload')
        print (len(files))
        for f in files:
            newFile = UploadFiles()
            newFile.files = f
            
            with open(f.title, 'wb+') as destination:
                for lines in destination.readlines():
                    print lines
            newFile.save()

        return HttpResponse('<h1 align="center">success</h1>')
    return render_to_response('upload.html')
    
def Menu(request):
#     user=request.GET['val']
    region_dic={
            'lizhaoning':{'age':20,'grade':100},
            'huangtao':{'age':20,'grade':99}
                }
    return HttpResponse(json.dumps(region_dic))
