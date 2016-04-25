from __future__ import absolute_import

from django.http import HttpResponse
from django.views.generic import TemplateView, View
{% set views = cookiecutter.views.split(' ') %}

class PingView(View):
    """
    Test if server is up
    """
    def get(self, request):  # pylint: disable=unused-argument
        return HttpResponse('pong')
{%- for view in views %}


class {{ view.capitalize() }}View(TemplateView):
    template_name = "{{ view }}.html"

    def get_context_data(self, **kwargs):
        context = super({{ view.capitalize() }}View, self).get_context_data(**kwargs)

        context.update({})

        return context
{%- endfor %}
