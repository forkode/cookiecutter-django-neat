"""Settings for all environments."""
import sys
from os import path

import environ
{%- if cookiecutter.use_sentry == 'y' %}
import raven
{%- endif %}

root = environ.Path(__file__) - 2
env = environ.Env(
    ALLOWED_HOSTS=(list, []),
    DEBUG=(bool, False),
{%- if cookiecutter.use_sentry == 'y' %}
    SENTRY_DSN=(str, ''),
{%- endif %}
)  # set default values and casting

if path.exists(str(root.path('.env'))):
    env.read_env(str(root.path('.env')))  # reading .env file

DEBUG = env('DEBUG')  # False if not in os.environ

public_root = root.path('static/')

MEDIA_ROOT = public_root('media')
MEDIA_URL = 'media/'
STATIC_ROOT = public_root('static')
STATIC_URL = '/static/static/'

# Raises ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = '[[ hooks.secret ]]'

ALLOWED_HOSTS = env('ALLOWED_HOSTS')

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    {%- if cookiecutter.use_sentry == 'y' %}
    'raven.contrib.django.raven_compat',
    {%- endif %}
    {%- if cookiecutter.use_rest_framework == 'y' %}
    'rest_framework',
    {%- endif %}
    '{{ cookiecutter.repo_name }}',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = '{{ cookiecutter.repo_name }}.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = '{{ cookiecutter.repo_name }}.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': env.db('DATABASE_URL', default='sqlite:///db.sqlite'),
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'stream': sys.stdout,
        },
{%- if cookiecutter.use_sentry == 'y' %}
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
{%- endif %}
    },
    'loggers': {
        'django': {
            'handlers': [
{%- if cookiecutter.use_sentry == 'y' %}
                'sentry',
{%- endif %}
                'console',
            ],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

{%- if cookiecutter.use_sentry == 'y' %}
try:
    release = raven.fetch_git_sha(root())
except raven.exceptions.InvalidGitRepository:
    release = 'unknown'

RAVEN_CONFIG = {
    'dsn': env('SENTRY_DSN'),
    'release': release,
}
{%- endif %}

# if 'test' in sys.argv:
#     DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}

if DEBUG:
    INSTALLED_APPS += (
        'debug_toolbar',
        'django_extensions',
        'django_nose',
    )

    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

    TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

    NOSE_ARGS = [
        '--with-coverage',
        '--cover-package={{ cookiecutter.repo_name }}',
        '--processes=8',
        '--cover-html',
    ]
