from django.conf.urls import patterns, include, url

from django.conf.urls.i18n import i18n_patterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = i18n_patterns('',
	url(r'^$', 'outside.views.index', name='outside_index'),
	url(r'^glue/', include('glue.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    #
    url(r'^', include('outside.urls')),
	
	#url(r'^news/$','hub.views.news', name='hub_news'),
    #url(r'^(?P<page_slug>[a-z0-9-]+)/$','hub.views.page', name='hub_page'),
    
    
)
