"""{{ cookiecutter.project_name }} URL configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
{%- if cookiecutter.use_rest_framework == 'y' %}
from rest_framework import routers
{%- endif %}

from {{ cookiecutter.repo_name}}.views import (
    PingView,
    {%- if cookiecutter.create_example_classes == 'y' %}
    MyView,
    {%- endif %}
)
{%- if cookiecutter.use_rest_framework == 'y' %}

router = routers.DefaultRouter()
#router.register('',,base_ name='')
{%- endif %}

urlpatterns = [
    path(r'admin/doc/', include('django.contrib.admindocs.urls')),
    path(r'admin/', admin.site.urls),
    path(r'ping', PingView.as_view(), name='ping'),
    {%- if cookiecutter.create_example_classes == 'y' %}
    path(r'my_view', MyView.as_view(), name='my_view'),
    {%- endif %}
    {%- if cookiecutter.use_rest_framework == 'y' %}
    path(r'api/', include(router.urls)),
    {%- endif %}
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
