# pylint: disable=wildcard-import, unused-wildcard-import
from settings.base import *

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'syslog': {
            'level': 'DEBUG',
            'class': 'logging.handlers.SysLogHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['syslog'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
