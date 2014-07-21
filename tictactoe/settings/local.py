"""
Django settings for tictactoe project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
# stdlib imports
import sys

# import project imports; see settings/base.py 
try:
	from .base import *
except ImportError:
	pass

TEMPLATE_DEBUG = DEBUG

DEBUG_TOOLBAR_PATCH_SETTINGS = False

# tuple that specifies the full python path to the order of displayed panel
DEBUG_TOOLBAR_PANELS = [
	'debug_toolbar.panels.versions.VersionsPanel',
	'debug_toolbar.panels.timer.TimerPanel',
	'debug_toolbar.panels.settings.SettingsPanel',
	'debug_toolbar.panels.headers.HeadersPanel',
	'debug_toolbar.panels.request.RequestPanel',
	'debug_toolbar.panels.sql.SQLPanel',
	'debug_toolbar.panels.staticfiles.StaticFilesPanel',
	'debug_toolbar.panels.templates.TemplatesPanel',
	'debug_toolbar.panels.cache.CachePanel',
	'debug_toolbar.panels.signals.SignalsPanel',
	'debug_toolbar.panels.logging.LoggingPanel',
	'debug_toolbar.panels.redirects.RedirectsPanel',
]

def show_toolbar(request):
	return True # always show toolbar, for example purposes only

DEBUG_TOOLBAR_CONFIG = {
	'SHOW_TOOLBAR_CALLBACK': 'settings.local.show_toolbar',
}

# django_debug_toolbar: required list or tuple for the built-in show_toolbar method
#INTERNAL_IPS = ('127.0.0.1',)
if DEBUG is True:
	class AllIPS(list):
		def __contains__(self, item):
			return True

	INTERNAL_IPS = AllIPS()

MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + (
	'debug_toolbar.middleware.DebugToolbarMiddleware',
)
################### END DEBUG CONFIGURATION


###################### APP CONFIGURATION
INSTALLED_APPS = INSTALLED_APPS + (
		'debug_toolbar',
)
################### END APP CONFIGURATION