__author__ = 'Jovi'

from scaffold.urls import *

urlpatterns.extend([
    url('^auth_login/', 'scaffold.spec.stage.views.auth_tmp_login'),
])