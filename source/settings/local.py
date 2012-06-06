# This is an example settings/local.py file.
# These settings overrides what's in settings/base.py

# To extend any settings from settings/base.py here's an example:
#from . import base
#INSTALLED_APPS = base.INSTALLED_APPS + ['debug_toolbar']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'source_demo_db',
    },
    #'default': {
    #    'ENGINE': 'django.db.backends.mysql',
    #    'NAME': 'source_db',
    #    'USER': 'root',
    #    'PASSWORD': '',
    #    'HOST': '',
    #    'PORT': '',
    #    'OPTIONS': {
    #        'init_command': 'SET storage_engine=InnoDB',
    #        'charset' : 'utf8',
    #        'use_unicode' : True,
    #    },
    #    'TEST_CHARSET': 'utf8',
    #    'TEST_COLLATION': 'utf8_general_ci',
    #},
}

# Uncomment this and set to all slave DBs in use on the site.
# SLAVE_DATABASES = ['slave']

# Recipients of traceback emails and other notifications.
ADMINS = (
    ('Ryan Pitts', 'ryan.a.pitts@gmail.com'),
)
MANAGERS = ADMINS

# Debugging displays nice error messages, but leaks memory. Set this to False
# on all server instances and True only for development.
DEBUG = TEMPLATE_DEBUG = True

# Is this a development instance? Set this to True on development/master
# instances and False on stage/prod.
DEV = True

# # Playdoh ships with sha512 password hashing by default. Bcrypt+HMAC is safer,
# # so it is recommended. Please read <https://github.com/fwenzel/django-sha2#readme>,
# # then switch this to bcrypt and pick a secret HMAC key for your application.
# PWD_ALGORITHM = 'bcrypt'
# HMAC_KEYS = {  # for bcrypt only
#     '2011-01-01': 'cheesecake',
# }

# Make this unique, and don't share it with anybody.  It cannot be blank.
SECRET_KEY = 'ke$fa^y$4f#%r4q$1zn@3az4&z6@kpw(ny4=isaozmta*6nv_r'

# Uncomment these to activate and customize Celery:
# CELERY_ALWAYS_EAGER = False  # required to activate celeryd
# BROKER_HOST = 'localhost'
# BROKER_PORT = 5672
# BROKER_USER = 'playdoh'
# BROKER_PASSWORD = 'playdoh'
# BROKER_VHOST = 'playdoh'
# CELERY_RESULT_BACKEND = 'amqp'

## Log settings

# SYSLOG_TAG = "http_app_playdoh"  # Make this unique to your project.
# LOGGING = dict(loggers=dict(playdoh={'level': logging.DEBUG}))

# Common Event Format logging parameters
#CEF_PRODUCT = 'Playdoh'
#CEF_VENDOR = 'Mozilla'