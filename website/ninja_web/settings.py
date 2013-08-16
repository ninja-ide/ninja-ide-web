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

TIME_ZONE = 'America/Argentina/Cordoba'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = False

MEDIA_ROOT = os.path.join(SITE_ROOT, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(SITE_ROOT, 'static')
STATIC_URL = '/static/'

#ADMIN_MEDIA_PREFIX = '/admin/media/'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
    #'django.template.loaders.eggs.Loader',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
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

SECRET_KEY = 'qwertyuiop'

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
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'django.contrib.admin',

    # Third party apps:
    'django_extensions',
    'debug_toolbar',
    'registration',
    'pagination',
    'south',
    #'profiles',
    'ninja_profiles',
    'tagging',
    'sorl.thumbnail',

    # Our apps:
    'common',
    'plugins',
    'schemes',
    'basic.blog',
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
