# encoding: utf-8
# Django settings for ninja_web project.

# default context_processors to be extended below
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

import os
SITE_ROOT = os.path.dirname(__file__.decode('utf-8'))

SETTINGS_PATH = os.path.abspath(os.path.dirname(__file__))

DEBUG = False
TEMPLATE_DEBUG = DEBUG
USE_LESSJS = False

ADMINS = (
    (u'Matías Herranz', 'matias@ninja-ide.org'),
    (u'Diego Sarmentero', 'dojo@ninja-ide.org'),
    (u'Pedro Mourelle', 'pedro@ninja-ide.org'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3'.
        'ENGINE': 'django.db.backends.',

        # Or path to database file if using sqlite3.
        'NAME': '',

        # Not used with sqlite3.
        'USER': '',

        # Not used with sqlite3.
        'PASSWORD': '',

        # Set to empty string for localhost. Not used with sqlite3.
        'HOST': '',

        # Set to empty string for default. Not used with sqlite3.
        'PORT': '',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = False

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
#MEDIA_ROOT = '/home/diegosarmentero/ninja-ide.org/public/media'
MEDIA_ROOT = os.path.join(SITE_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin/media/'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    # django-pagination
    'pagination.middleware.PaginationMiddleware',
)

ROOT_URLCONF = 'ninja_web.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or
    # "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(SITE_ROOT, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
    'ninja_web.context_processors.use_lessjs',
    'ninja_web.context_processors.user_info',
)

INSTALLED_APPS = (
    # Django stuff:
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',

    # Third party apps:
    'django_extensions',
    'registration',
    'pagination',
    'south',
    'profiles',
    'ninja_profiles',
    'tagging',
    # 'compressor',

    # Our apps:
    'common',
    'plugins',
    'schemes',
)

## django-registration
# This is the number of days users will have to activate their
# accounts after registering. If a user does not activate within
# that period, the account will remain permanently inactive and may
# be deleted by maintenance scripts provided in django-registration.
ACCOUNT_ACTIVATION_DAYS = 7
LOGIN_REDIRECT_URL = '/'

AUTH_PROFILE_MODULE = 'ninja_profiles.NinjaProfile'

# Email settings:
USER = 'username@gmail.com'
PSWD = 'pswd'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = USER
EMAIL_HOST_PASSWORD = PSWD
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Import local_settings file
from local_settings import *
