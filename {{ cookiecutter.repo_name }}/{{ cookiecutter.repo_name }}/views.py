"""{{ cookiecutter.project_name }} views."""
from django.http import HttpResponse
from django.views.generic import View
{%- if cookiecutter.create_example_classes == 'y' %}from django.views.generic import TemplateView{%- endif %}
{%- if cookiecutter.use_rest_framework == 'y' %}
from rest_framework import viewsets
{%- endif %}


class PingView(View):
    """Test if server is up."""

    def get(self, request):  # pylint: disable=unused-argument
        """Pong response."""
        return HttpResponse('pong')
{%- if cookiecutter.create_example_classes == 'y' %}


class MyView(TemplateView):
    template_name = "my_template.html"

    def get_context_data(self, **kwargs):
        context = super(MyView, self).get_context_data(**kwargs)

        context.update({})

        return context
{%- endif %}
