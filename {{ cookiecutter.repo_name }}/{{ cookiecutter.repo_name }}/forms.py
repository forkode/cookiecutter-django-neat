"""{{ cookiecutter.project_name }} forms."""
{%- if cookiecutter.create_example_classes == 'y' %}
from django import forms


class MyForm(forms.Form):
    integer_field = forms.IntegerField(required=False)
{%- endif %}
