from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from loader import Loader
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


def json_view(request, subview_name):
    Loader().load()
    return HttpResponse(json.dumps({}), content_type="application/json")


def reload_view(request, subview_name):
    Loader().load()
    f = subviews[subview_name]
    res = f(request)
    response = {}
    response['html_string'] = res[0]
    response['id'] = res[1]['id']

    return HttpResponse(json.dumps(response), content_type="application/json")
