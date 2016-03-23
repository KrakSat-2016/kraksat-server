"""
Local settings for kraksat_server project.
"""

from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'opg%a_8uwrnz#u7w&%19*_g732!a6g1i#pr7v78%0+%i9tdr*v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CORS_ORIGIN_ALLOW_ALL = True
