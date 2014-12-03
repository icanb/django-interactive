from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from base import (
    html_view,
    json_view,
    reload_view
)

urlpatterns = patterns('',
    url(r"^(?P<subview_name>.+)/json/$", json_view, name="get_json"),
    url(r"^(?P<subview_name>.+)/html/$", html_view, name="get_html"),
    url(r"^(?P<subview_name>.+)/reload/$", reload_view, name="reload_html"),
)