##################
# LOCAL SETTINGS #
##################

# Allow any settings to be defined in local_settings.py which should be
# ignored in your version control system allowing for settings to be
# defined per machine.

from base import *

DEBUG = True
LESS_DEBUG = True
LESS_EXECUTABLE = "node_modules/less/bin/lessc"
COMPRESS_ENABLED = not DEBUG

TEST_RUNNER = 'django.test.simple.DjangoTestSuiteRunner'

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}

try:
    from local import *
except ImportError:
    pass

dev_compress = []
for preprocessor_type, processor_call in COMPRESS_PRECOMPILERS:
    if preprocessor_type == "text/less":
        processor_call = LESS_EXECUTABLE + " {infile} {outfile}"
    dev_compress.append((preprocessor_type, processor_call))
COMPRESS_PRECOMPILERS = tuple(dev_compress)

run_checkers(globals())
