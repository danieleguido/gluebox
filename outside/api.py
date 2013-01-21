from django.db import IntegrityError 
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.conf import settings
from glue.models import Pin
from glue.misc import Epoxy, API_EXCEPTION_FORMERRORS, API_EXCEPTION_INTEGRITY
from outside.models import Subscriber
from outside.forms import SubscriberForm


#
#    API CUSTOM DECORATORS
#    =====================
#
def is_editor(user):
	if user:
		return user.groups.filter(name='CONTENT EDITOR').count() != 0
	return False


#
#    API AUTH VIEWS
#    ==============
#
API_ACCESS_DENIED_URL = "/elipss/panelmanager/api/access-restricted"


def enquete_data( request, enquete_id ):
	data = {}
	return render_to_response('outside/enquete_data.json', RequestContext(request, data ) )

def subscribers(request):
	# logger.info("Welcome to GLUEBOX api")
	response = Epoxy( request )
	if response.method=="POST":

		form = SubscriberForm( request.REQUEST )
		
		if not form.is_valid():
			return response.throw_error( error=form.errors, code=API_EXCEPTION_FORMERRORS).json()
		try:
			s = Subscriber(
				first_name = form.cleaned_data['first_name'],
				last_name = form.cleaned_data['last_name'],
				email = form.cleaned_data['email'],
				affiliation = form.cleaned_data['affiliation'],
				accepted_terms = form.cleaned_data['accepted_terms'],
				description = form.cleaned_data['description']).save()
		except IntegrityError, e:
			return response.throw_error( error="%s" % e, code=API_EXCEPTION_INTEGRITY).json()

	return response.queryset( Subscriber.objects.filter() ).json()
	

def subscriber( request, subscriber_id ):
	return Epoxy( request ).single( Subscriber, {'id':subscriber_id} ).json()

