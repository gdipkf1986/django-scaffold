# -*- coding: utf-8 -*-
from scaffold.settings import *
from scaffold.spec.stage import *

DEBUG = True
GOP_OAUTH_SITE = "https://testconnect.garena.com"
GOP_OAUTH_CALLBACK = "http://127.0.0.1:<port>"
TEMPLATE_DEBUG = True
LOGGER = 'app.default'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'scaffold_stage',
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

WSGI_APPLICATION = 'scaffold.spec.stage.wsgi.application'

# MIDDLEWARE_CLASSES += (
#     'scaffold.spec.stage.midware_tmp_auth.tmp_auth',
# )

TEMPLATE_DIRS += (
    os.path.join(BASE_DIR, 'scaffold/spec/stage/templates'),
)

ROOT_URLCONF = 'scaffold.spec.stage.urls'

print "---------------------------------------------------"
print "lauching with stage setting, you can change it in manage.py or 'run/debug configuration/enviroments variables/DJANGO_SETTINGS_MODULE' in pycharm"
print "---------------------------------------------------"
