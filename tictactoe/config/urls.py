from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from pages import views

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'tictactoe.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', views.home),
)
