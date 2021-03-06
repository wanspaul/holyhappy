"""
Django settings for holyhappy project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-u14eqr@0jv0%d7n99u77m+$z3*y^i^_jx^ex9%7!h&$6g6!zt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'raven.contrib.django.raven_compat',
    'pray',
    'newsongy',
    'bible'
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

ROOT_URLCONF = 'holyhappy.urls'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'holyhappy.utils.authentication.CustomAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'holyhappy.utils.permission.CustomPermission',
    ),
    'EXCEPTION_HANDLER': 'holyhappy.utils.custom_exception_handler.custom_exception_handler'
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            PROJECT_PATH + '/templates/',
            ],
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

WSGI_APPLICATION = 'holyhappy.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

COOKIE_DOMAIN = '127.0.0.1'

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=6),
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
TIME_ZONE = 'Asia/Seoul'

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join('static'), )

REDIS_HOST = '127.0.0.1'
REDIS_PORT = '6579'

LOGGING = {
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': 'MARTIAN %(levelname)s %(asctime)s %(message)s'
        },
        'template': {
            'format': 'TEMPLATE %(levelname)s %(asctime)s %(message)s'
        },
        'db': {
            'format': 'DB %(levelname)s %(asctime)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'version': 1,
    'handlers': {
        'console': {
            # logging handler that outputs log messages to terminal
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',  # message level to be written to console
            'formatter': 'verbose',
        },
        'console_template': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'template'
        },
        'console_db': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'db'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/tmp/holyhappy.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        '': {
            # this sets root level logger to log debug and higher level
            # logs to console. All other loggers inherit settings from
            # root level logger.
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,  # this tells logger to send logging message
            # to its parent (will send if set to True)
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.template': {
            'handlers': ['console_template'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console_db'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}
