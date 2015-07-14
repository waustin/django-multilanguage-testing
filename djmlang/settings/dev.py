from base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# CACHE CONFIG
CACHES = {
   'default': {
       'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
   }
}
ALLOWED_HOSTS = ['*']

# DJANGO DEBUG TOOLBAR
#MIDDLEWARE_CLASSES += (
#    'debug_toolbar.middleware.DebugToolbarMiddleware',
#)

#INSTALLED_APPS += (
#    'debug_toolbar',
#)
#DEBUG_TOOLBAR_CONFIG = {
    # If set to True (default), the debug toolbar will show an intermediate
    # page upon redirect so you can view any debug information prior to
    # redirecting. This page will provide a link to the redirect destination
    # you can follow when ready. If set to False, redirects will proceed as
    # normal.
#    'INTERCEPT_REDIRECTS': False,

    # If not set or set to None, the debug_toolbar middleware will use its
    # built-in show_toolbar method for determining whether the toolbar should
    # show or not. The default checks are that DEBUG must be set to True and
    # the IP of the request must be in INTERNAL_IPS. You can provide your own
    # method for displaying the toolbar which contains your custom logic. This
    # method should return True or False.
#    'SHOW_TOOLBAR_CALLBACK': None,

    # An array of custom signals that might be in your project, defined as the
    # python path to the signal.
#    'EXTRA_SIGNALS': [],

    # If set to True (the default) then code in Django itself won't be shown in
    # SQL stacktraces.
#    'HIDE_DJANGO_SQL': True,

    # If set to True (the default) then a template's context will be included
    # with it in the Template debug panel. Turning this off is useful when you
    # have large template contexts, or you have template contexts with lazy
    # datastructures that you don't want to be evaluated.
#    'SHOW_TEMPLATE_CONTEXT': True,

    # If set, this will be the tag to which debug_toolbar will attach the debug
    # toolbar. Defaults to 'body'.
#    'TAG': 'body',
#}

#INTERNAL_IPS = ('127.0.0.1',)

# EMAIL CONFIGURATION
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

# options
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = False


# SWITCH STORAGE TO S3
#  DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'mystorage.custom_storages.MediaStorage'
DEFAULT_S3_PATH = 'uploads'

#MEDIA_ROOT = '/%s/' % DEFAULT_S3_PATH
MEDIA_ROOT = ''

# STORAGES STUFF
MEDIAFILES_LOCATION = DEFAULT_S3_PATH

# STATIC FILES S3
STATICFILES_STORAGE = 's3_folder_storage.s3.StaticStorage'
STATIC_S3_PATH = 'static'
STATIC_ROOT = "/%s/" % STATIC_S3_PATH

STATIC_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/' + STATIC_S3_PATH + '/'
MEDIA_URL =  'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/' + DEFAULT_S3_PATH + '/'

