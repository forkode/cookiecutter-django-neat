"""{{ cookiecutter.project_name }} models."""
{%- if cookiecutter.create_example_classes == 'y' %}
from django.db import models


class MyModel(models.Model):
    char_field = models.CharField(max_length=255)
    integer_field = models.IntegerField()
{%- endif %}
