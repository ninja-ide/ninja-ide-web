# -*- coding: utf-8 -*-
# LOCAL Django settings template for ninja_web project.
# place your local settings here.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
         # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3'.
        'ENGINE': 'sqlite3',

        # Or path to database file if using sqlite3.
        'NAME': 'ninja_ide.db',

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

# Make this unique, and don't share it with anybody.
SECRET_KEY = 't!$37#m_5t+2_2@7zg2x9nz#zq1uw@@=^cn=xikdy_m*14la$$'

# Email settings:
USER = 'asdf@gmail.com'
PSWD = 'asdfasdf'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = USER
EMAIL_HOST_PASSWORD = PSWD
EMAIL_PORT = 587
EMAIL_USE_TLS = True
