# stdlib 
import pdb

# django core
from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

#from pages import views

#*********** DEVELOPMENT --  models to use -- DEVELOPMENT ***********************
from settings.base import STATIC_ROOT
from settings.base import MEDIA_URL
from settings.base import MEDIA_ROOT
from settings.base import DEBUG
#from settings.base import get_env_variable
# *********************************************************************************

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'tictactoe.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'pages.views.home', name='home'),
	url(r'^$', 'ai.views.tictactoeviews', name="tictactoe"),
)

if 'settings.local':
	import debug_toolbar
	# adding static function to the end of the urlpatterns tells development server to map the 
	# MEDIA_URL to the files in the MEDIA_ROOT.
	urlpatterns += patterns('',
		url(r'^__debug__/', include(debug_toolbar.urls)),
	)
	urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

#elif get_env_variable('SETTINGS_ENVIRONMENT') == 'settings.staging' or get_env_variable('SETTINGS_ENVIRONMENT') == 'settings.production':
#	# for admin static files on heroku
#	urlpatterns += patterns('',
#		url(r'^static/(?P<path>.*)$', 'django.contrib.staticfiles.views.serve', {
#			'document_root': STATIC_ROOT,
#		}),
#	 )
