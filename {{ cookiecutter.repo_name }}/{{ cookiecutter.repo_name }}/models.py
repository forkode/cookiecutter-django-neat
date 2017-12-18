"""{{ cookiecutter.project_name }} models."""
from django.db import models
{%- if cookiecutter.create_example_classes == 'y' %}


class MyModel(models.Model):
    char_field = models.CharField(max_length=255)
    integer_field = models.IntegerField()
{%- endif %}
