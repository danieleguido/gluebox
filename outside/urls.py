from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
	url(r'^$','outside.views.index', name='outside_index'),
	url(r'^login/$','outside.views.login_view', name='outside_login'),
	url(r'^logout/$','outside.views.logout_view', name='outside_logout'),
	
	url(r'^news/$','outside.views.news', name='outside_news'),
	url(r'^(?P<page_slug>[a-z0-9-]+)/$','outside.views.page', name='outside_page'),
)