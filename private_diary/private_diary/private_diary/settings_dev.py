from . settings_common import *

DEBUG = True

ALLOWED_HOSTS = []

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'logger':{
        'django':{
            'handlers': ['console'],
            'level': 'INFO',
        },
        'diary':{
            'handlers':['console'],
            'lebel': 'DEBUG',
        },
    },

    'handlers':{
         'console':{
             'level':'DEBUG',
             'class':'logging.StreamHandler',
             'formatter':'dev',
         },
    },

    'formatters':{
        'dev':{
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ]
            )
        },
    }

}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

