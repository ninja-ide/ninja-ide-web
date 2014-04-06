#######################
# PRODUCTION SETTINGS #
#######################

from base import *


DEBUG = False
LESS_DEBUG = False

TEST_RUNNER = 'django.test.simple.DjangoTestSuiteRunner'

# all private settings to config production environment
# should exist in a separated AND NOT VERSIONED file (prod_private).

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": "dev.db",
#         "USER": "",
#         "PASSWORD": "",
#         "HOST": "",
#         "PORT": "",
#     }
# }

try:
    from local import *
except ImportError:
    print("Production settings file not found. Ensure you have a "\
          "'prod_private' file (not versioned)")

run_checkers(globals())
