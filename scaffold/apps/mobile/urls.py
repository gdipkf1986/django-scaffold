__author__ = 'Jovi'
from django.conf.urls import patterns,  url

from scaffold.apps.mobile import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)