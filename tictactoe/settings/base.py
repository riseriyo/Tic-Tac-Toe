"""
Django settings for tictactoe project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
# stdlib imports
from os.path import join, abspath, dirname
import os
import logging
logger = logging.getLogger(__name__)

# django core
# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured

#  project's imports


def get_env_variable(var_name):
	"""Get the environment variable or return exception"""
	try:
		return os.environ[var_name]
	except KeyError:
		error_msg = "Set the %s environment variable" % var_name
		raise ImproperlyConfigured(error_msg)


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

################### SECRET CONFIGURATION
# Make this unique, and don't share it with anybody.
SECRET_KEY = get_env_variable('TTT_SECRET_KEY')

###################### DEBUG CONFIGURATION
DEBUG = bool(os.environ.get('DEBUG',False))

###################### END DEBUG CONFIGURATION

ALLOWED_HOSTS = []


# Application definition
###################### APP CONFIGURATION
DJANGO_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	# Uncomment the next line to enable the admin:
	'django.contrib.admin',
	# Uncomment the next line to enable admin documentation:
	#'django.contrib.admindocs',

)

THIRD_PARTY_APPS = (
	'south',
)

LOCAL_APPS = (
	'pages',
	'ai',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
######################## END APP CONFIGURATION

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

###################### STATIC CONFIGURATION
# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'templates/static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
	os.path.join(BASE_DIR, 'static'),
)
###################### END STATIC CONFIGURATION

###################### TEMPLATE CONFIGURATION
TEMPLATE_CONTEXT_PROCESSORS = (
								"django.contrib.auth.context_processors.auth",
								"django.core.context_processors.debug",
								"django.core.context_processors.i18n",
								"django.core.context_processors.media",
								"django.core.context_processors.static",
								"django.core.context_processors.tz",
								"django.contrib.messages.context_processors.messages",
								'django.core.context_processors.request',
								)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
#	 'django.template.loaders.eggs.Loader',
)
TEMPLATE_DIRS = (
	os.path.join(BASE_DIR, 'templates'),
)
###################### END TEMPLATE CONFIGURATION

###################### MEDIA CONFIGURATION
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
#MEDIA_ROOT = os.path.join(ROOT, 'media')
MEDIA_ROOT = '/media/'

MEDIA_URL = '/media/'
# URL prefix for admin static files -- CSS, JS and images; must use trailing slash;
ADMIN_MEDIA_PREFIX = '/static/admin/'
###################### END MEDIA CONFIGURATION