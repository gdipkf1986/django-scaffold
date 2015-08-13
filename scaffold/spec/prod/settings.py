# -*- coding: utf-8 -*-
from scaffold.settings import *

WSGI_APPLICATION = 'scaffold.spec.prod.wsgi.application'

GOP_OAUTH_SITE = "https://testconnect.garena.com"
GOP_OAUTH_CALLBACK = "http://127.0.0.1:<port>"
TEMPLATE_DEBUG = False
LOGGER = 'app.default'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<database_name>',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',  # Set to empty string for default.
    },
    # 'extra_db': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': '<database_name>',
    #     'USER': '',
    #     'PASSWORD': '',
    #     'HOST': '',
    #     'PORT': '6606',
    # }
}


print "---------------------------------------------------"
print "lauching with production setting, you can change it in manage.py or 'run/debug configuration/enviroments variables/DJANGO_SETTINGS_MODULE' in pycharm"
print "---------------------------------------------------"
