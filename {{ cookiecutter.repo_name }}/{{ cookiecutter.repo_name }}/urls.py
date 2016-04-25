from __future__ import absolute_import

from django.conf.urls import include, url
from django.contrib import admin

{% set views = cookiecutter.views.split(' ') -%}
from {{ cookiecutter.repo_name}}.views import (
    PingView,
    {%- for view in views %}
    {{ view.capitalize() }}View,
    {%- endfor %}
)

urlpatterns = [
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ping', PingView.as_view(), name='ping'),
    {%- for view in views %}
    url(r'^{{ view }}$', {{ view.capitalize() }}View.as_view(), name='{{ view }}'),
    {%- endfor %}
]
