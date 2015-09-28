# -*- coding: utf-8 -*-
from .base import *

SECRET_KEY = ')0*14wp#g8si#31c6&$)^(3n_$dc!jipnh79ql1tus!%(b9&o-'

DEBUG = True
TEMPLATE_DEBUG = DEBUG


DATABASES = {
    'default': {
        'NAME': 'demo_db',
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'USER': 'demo_user',
        'PASSWORD': 'demo_pass',
        'HOST': '127.0.0.1'
    },

}


STATIC_ROOT = '/var/www/staticciuccit.noip.me/'
MEDIA_ROOT = '/var/www/mediaciuccit.noip.me/'

SITE_URL = 'http://ciuccit.noip.me'
MEDIA_URL = 'http://mediaciuccit.noip.me/'
STATIC_URL = 'http://staticciuccit.noip.me/'

SITE_NAME = "http://ciuccit.noip.me"


# Hosts/domain names that are valid for this site; required if DEBUG is False
ALLOWED_HOSTS = ['ciuccit.noip.me',]
