__author__ = 'Jovi'

from scaffold.urls import *

urlpatterns.append(
    url('^auth_login/', 'scaffold.spec.stage.views.auth_tmp_login'),
)