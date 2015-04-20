__author__ = 'Jovi'

from django.shortcuts import HttpResponseRedirect

users = {
    "user-001": "861b6",
    "user-002": "55134",
}


class tmp_auth(object):
    def process_request(self, request):
        if request.path != '/auth_login/':
            if 'granted' not in request.session or request.session['granted'] is not True:
                return HttpResponseRedirect("/auth_login/")
            else:
                return None
        else:
            return None