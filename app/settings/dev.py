# -*- coding: utf-8 -*-
from .base import *

SECRET_KEY = ')0*14wp#g8si#31c6&$)^(3n_$dc!jipnh79ql1tus!%(b9&o-'

DEBUG = True
TEMPLATE_DEBUG = DEBUG


DATABASES = {
    'default': {
        'NAME': 'ciuccit',
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'USER': 'vagrant',
        'PASSWORD': 'vagrant',
        'HOST': '127.0.0.1'
    },

}
