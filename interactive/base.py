"""
This module includes the basic Layout class and basic methods for layout 
implementation.

"""

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from loader import Loader
from django.db.models.query import QuerySet
import json

subviews = {}

class Layout(object):

    def register_subview(self, render_func, name=None, **flags):
        if name is not None and render_func is not None:
            subviews[name] = render_func
        elif name is None and render_func is not None:
            name = render_func.__name__
            subviews[name] = render_func
        else:
            raise Exception("Unsupported arguments to register_subview")


def html_view(request, subview_name):
    Loader().load()
    f = subviews[subview_name]
    return HttpResponse(f(request)[0])


def eval_dict(dict_val):
    new_dict = {}
    for key, value in dict_val.items():
        new_dict[key] = eval_value(value)
    return new_dict


def eval_list(list_val):
    list_result = [eval_value(entry) for entry in list_val]
    return list_result


def eval_value(value):
    if isinstance(value, dict):
        return eval_dict(value)
    if isinstance(value, list):
        return eval_list(value)
    elif isinstance(value, basestring):
        return value
    elif isinstance(value, int):
        return value
    elif type(value) is QuerySet:
        result = value.values()
        list_result = [entry for entry in result]
        return list_result
    else:
        return None


def json_view(request, subview_name):
    Loader().load()

    f = subviews[subview_name]
    context = f(request)[1]
    json_dict = {}    

    if context is not None:
        json_dict = eval_dict(context)

    return HttpResponse(json.dumps(json_dict), content_type="application/json")


def reload_view(request, subview_name):
    Loader().load()
    f = subviews[subview_name]
    res = f(request)
    response = {}
    response['html_string'] = res[0]
    response['id'] = res[1]['id']

    return HttpResponse(json.dumps(response), content_type="application/json")
