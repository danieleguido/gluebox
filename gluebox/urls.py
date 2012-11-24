from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'outside.views.index', name='outside_index'),
	url(r'^oo/', include('outside.urls')),
	url(r'^glue/', include('glue.urls')),

    # Examples:
    # url(r'^$', 'gluebox.views.home', name='home'),
    # url(r'^gluebox/', include('gluebox.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
