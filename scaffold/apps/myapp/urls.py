__author__ = 'Jovi'
from django.conf.urls import patterns, include, url

from scaffold.apps.myapp import  views

urlpatterns = patterns('',
    url(r'^$', views.welcome, name='welcome'),
)