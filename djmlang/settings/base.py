"""
Django settings for djmlang project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
import os
import sys

PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(PROJECT_DIR)

# App/Library Paths
sys.path.append(os.path.join(BASE_DIR, 'apps'))

# Users TO EMAIL Errors to based on LOGGING Settings
ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p%af4@vnrnd%os7=i$#3e7$@5nvo*-280en3r*34!ld1psb7+='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

# DATABASE Configured by URL
import dj_database_url
DATABASES = {'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))}

INSTALLED_APPS = (

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'modeltranslation',

    # Grappelli and Filebrowser Admin - must come before the admin
    'grappelli',
    'filebrowser',
    'django.contrib.admin',
    'django_extensions',
    'storages',  # storages redux
    's3_folder_storage',
    'mptt',
    'pages',
    'easy_thumbnails',
    'redactor',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'djmlang.urls'

WSGI_APPLICATION = 'djmlang.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False


# Upload Media
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'uploads')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/uploads/'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'assets'),
)

# Template Settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# DATABASE Configured by URL
import dj_database_url
DATABASES = {'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))}

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

from django.utils.translation import ugettext_lazy as _
LANGUAGES = (
    ('en', _('English')),
    ('es', _('Spanish')),
)

# MODEL TRANSLATION STUFF
MODELTRANSLATION_PREPOPULATE_LANGUAGE = 'en'

# SUPPRESS FACTORY BOY LOGGING MESSAGES
import logging
logging.getLogger("factory").setLevel(logging.WARN)

# APP SETTINGS
GRAPPELLI_ADMIN_TITLE = 'Translation Website Admin'

# FILEBROWSER SETTINGS
FILEBROWSER_DEBUG = True
FILEBROWSER_DIRECTORY = ''

FILEBROWSER_NORMALIZE_FILENAME = True

# Allow FileBrowser Extensions
FILEBROWSER_EXTENSIONS = {
    'Folder': [''],
    'Image': ['.jpg', '.jpeg', '.gif', '.png'],
    'Document': ['.pdf', '.txt', '.doc', '.rtf', '.xls'],
    'Audio': ['.mp3'],
    'Video': ['.mp4']
}

FILEBROWSER_VERSIONS = {
    'admin_thumbnail': {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop upscale'},
    'thumbnail': {'verbose_name': 'Thumbnail (100px) Square', 'width': 100, 'height': '100', 'opts': 'crop'},
    'small': {'verbose_name': 'Small (150px Wide)', 'width': 150, 'height': '', 'opts': ''},
    'medium': {'verbose_name': 'Medium (300px Wide)', 'width': 300, 'height': '', 'opts': ''},
    'big': {'verbose_name': 'Big (500px Wide)', 'width': 500, 'height': '', 'opts': ''},
    'large': {'verbose_name': 'Large (700px Wide)', 'width': 700, 'height': '', 'opts': ''},
    'x-large': {'verbose_name': 'Extra Large (900px Wide)', 'width': 900, 'height': '', 'opts': ''},
}

# EASY THUMBNAILS
THUMBNAIL_SUBDIR = '_thumbs'


# AWS STUFF - Read from env
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

# For Django extensions sync command
AWS_BUCKET_NAME = AWS_STORAGE_BUCKET_NAME

AWS_HEADERS = {
     'Expires': 'Thu, 15 Apr 2010 20:00:00 GMT',
     'Cache-Control': 'max-age=86400',
}

SYNC_S3_PREFIX = 'uploads'


# APP STUFF
PAGES_HEADER_IMAGE_DIR = ''


REDACTOR_OPTIONS = {'lang': 'en'}
REDACTOR_UPLOAD = os.path.join(MEDIA_ROOT, 'pages')
