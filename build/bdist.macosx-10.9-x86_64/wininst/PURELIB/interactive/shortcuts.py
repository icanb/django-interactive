from django.http import HttpResponse
from django.template import loader, RequestContext
from django.shortcuts import render as django_render
from stub import StubGenerator
from base import subviews

from pyquery import PyQuery as pq

def render_subview(request, *args, **kwargs):

    """
    Returns a HttpResponse whose content is filled with the result of calling
    django.template.loader.render_to_string() with the passed arguments.
    Uses a RequestContext by default.
    """
    httpresponse_kwargs = {
        'content_type': kwargs.pop('content_type', None),
        'status': kwargs.pop('status', None),
    }

    context = args[1]

    if 'context_instance' in kwargs:
        context_instance = kwargs.pop('context_instance')
        if kwargs.get('current_app', None):
            raise ValueError('If you provide a context_instance you must '
                             'set its current_app before calling render()')
    elif request is "custom_tag":
        ## means that the request is coming from custom template tag
        html_str = loader.render_to_string(*args, **kwargs)
        return html_str
    else:
        current_app = kwargs.pop('current_app', None)
        context_instance = RequestContext(request, current_app=current_app)

    kwargs['context_instance'] = context_instance
    html_str = loader.render_to_string(*args, **kwargs)

    # settings up the wrapper element
    if 'el' in context:
        open_tag = "<"+ context['el']+ " id=" + context['id'] + ">"
        close_tag = "</"+ context['el']+ ">"
        html_str = open_tag + html_str + close_tag

    return (html_str, context)


def render_pageview(request, *args, **kwargs):

    """
    Returns a HttpResponse whose content is filled with the result of calling
    django.template.loader.render_to_string() with the passed arguments.
    Uses a RequestContext by default.
    """
    httpresponse_kwargs = {
        'content_type': kwargs.pop('content_type', None),
        'status': kwargs.pop('status', None),
    }

    if 'context_instance' in kwargs:
        context_instance = kwargs.pop('context_instance')
        if kwargs.get('current_app', None):
            raise ValueError('If you provide a context_instance you must '
                             'set its current_app before calling render()')
    else:
        current_app = kwargs.pop('current_app', None)
        context_instance = RequestContext(request, current_app=current_app)

    kwargs['context_instance'] = context_instance

    js_string = '<script type="text/javascript">\n' + StubGenerator(subviews).generate_javascript() + '</script>\n'

    html_str = loader.render_to_string(*args, **kwargs)
    el = pq(html_str)
    el.find('head').append(js_string)
    html_str = el.html()

    return HttpResponse(html_str)


