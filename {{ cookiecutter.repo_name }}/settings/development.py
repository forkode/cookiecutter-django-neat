# pylint: disable=wildcard-import, unused-wildcard-import
from settings.base import *

INSTALLED_APPS += (
    'debug_toolbar',
    'django_extensions',
    'django_nose',
    {% if cookiecutter.use_rest_framework == 'y' -%}
      'django_rest_framework_generator',
    {%- endif %}
    '{{ cookiecutter.repo_name }}',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--with-coverage',
    '--cover-package={{ cookiecutter.repo_name }}',
    '--processes=8',
]
