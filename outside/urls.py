from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
	url(r'^$','outside.views.index', name='outside_index'),
	url(r'^login/$','outside.views.login_view', name='outside_login'),
	url(r'^logout/$','outside.views.logout_view', name='outside_logout'),
	url(r'^download/(?P<pin_slug>[a-z0-9-_]+)/$','outside.views.download_view', name='outside_download'),

	# special pages before auto /page
	url(r'^news/$','outside.views.news', name='outside_news'),
	url(r'^index/$','outside.views.index', name='outside_index'),

	
	# api outside specific: subscribers etc...
	url(r'^api/subscriber/$', 'outside.api.subscribers', name='outside_api_subscribers'),
	url(r'^api/subscriber/(?P<subscriber_id>\d+)/$', 'outside.api.subscriber', name='outside_api_subscriber'),
	
	#login
	url(r'^api/login/$', 'outside.api.login', name='outside_api_login'),

	# url(r'^blog/$','outside.views.news', name='outside_news'), # a special page for blog posting with comments on page
	url(r'^(?P<page_slug>[a-z0-9-]+)/$','outside.views.page', name='outside_page'),
)
