from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'hub.views.index', name='hub_index'),
	# url(r'^captcha/', include('captcha.urls')),
	url(r'^glue/', include('glue.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    #
    url(r'^o/', include('outside.urls')),
	
    url(r'^(?P<page_slug>[a-z0-9-]+)/$','hub.views.page', name='hub_page'),
    
    
)
