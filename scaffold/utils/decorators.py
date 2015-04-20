__author__ = 'Jovi'

from django.shortcuts import HttpResponse
import json


def log_func(log):
    def wrap(func):
        def func_wrapper(*args, **kwargs):
            log.debug("%s:" % func)
            for i, arg in enumerate(args):
                log.debug("\targs-%d: %s" % (i + 1, arg))
            for k, v in enumerate(kwargs):
                log.debug("\tdict args: %s: %s" % (k, v))
            return func(*args, **kwargs)

        return func_wrapper

    return wrap


def json_response(view):
    def wrapper(request, *args, **kwargs):
        json_dict = view(request, *args, **kwargs)
        response = HttpResponse(json.dumps(json_dict))
        response['content-Type'] = 'application/json'
        return response
    return wrapper
