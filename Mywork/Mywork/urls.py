"""Mywork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from app01 import views
from ssh.views import SSH,Connect,log,SendCommand
import settings

urlpatterns = [
    url(r'^statics/(?P<path>.*)', 'django.views.static.serve',{'document_root':settings.STATIC_PATH}),           
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.Index),
    url(r'^index/', views.Index),
    url(r'^region/$', views.Menu),
]
#login & logout
urlpatterns += [
    url(r'^login/', views.Login),
    url(r'^auth/$', views.Auth),
    url(r'^logout/$',views.Logout)
]
#upload
urlpatterns += [
    url(r'^upload/$', views.uploadFile),
]
#ssh
urlpatterns += [
    url(r'^ssh/$', SSH),
    url(r'^connect/$', Connect),
    url(r'^send/$', SendCommand),
    url(r'^log/$', log),
]
#test
urlpatterns += [
    url(r'^region/$', views.Menu),
]


