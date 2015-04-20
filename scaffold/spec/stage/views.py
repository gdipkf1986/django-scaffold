__author__ = 'Jovi'

from django.shortcuts import render, redirect
from django.shortcuts import HttpResponseRedirect
from scaffold.spec.stage import midware_tmp_auth


def auth_tmp_login(request):
    if 'uname' in request.POST and 'upass' in request.POST:
        uname = request.POST['uname']
        upass = request.POST['upass']
        if uname not in midware_tmp_auth.users or (midware_tmp_auth.users[uname] != upass):
            return render(request, 'login.html', {'error': True})
        else:
            request.session['granted'] = True
            return redirect('mobile')
    else:
        return render(request, 'login.html', {'error': False})


def auth_tmp_logout(request):
    request.session['granted'] = False
    return HttpResponseRedirect("/")

