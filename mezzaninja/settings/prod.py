#######################
# PRODUCTION SETTINGS #
#######################

from base import *


DEBUG = False
LESS_DEBUG = False

TEST_RUNNER = 'django.test.simple.DjangoTestSuiteRunner'

# all private settings to config production environment
# should exist in a separated AND NOT VERSIONED file (prod_private).

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "dev.db",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    }
}


ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"

LESS_EXECUTABLE = "/home/ninjaide/webapps/node/node_modules/less/bin/lessc"

dev_compress = []
for preprocessor_type, processor_call in COMPRESS_PRECOMPILERS:
    if preprocessor_type == "text/less":
        processor_call = LESS_EXECUTABLE + " {infile} {outfile}"
    dev_compress.append((preprocessor_type, processor_call))
COMPRESS_PRECOMPILERS = tuple(dev_compress)

run_checkers(globals())
