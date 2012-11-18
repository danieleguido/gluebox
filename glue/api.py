import logging

from django.db.models.loading import get_model
from glue.misc import Epoxy
from glue.models import Page, Pin

logger = logging.getLogger(__name__)

def index(request):
	# logger.info("Welcome to GLUEBOX api")
	return Epoxy( request ).json()

def manage_objects( request, model_name ):
	# logger.info("Welcome to GLUEBOX api")
	return Epoxy( request ).queryset( get_model( "glue", model_name ).objects.filter(), model_name=model_name ).json()

def manage_single_object( request, model_name, pk ):
	# logger.info("Welcome to GLUEBOX api")
	return Epoxy( request ).single( Page, {'pk':pk} ).json()

def pages(request):
	# logger.info("Welcome to GLUEBOX api")
	return Epoxy( request ).queryset( Page.objects.filter() ).json()

def page( request, page_id ):
	return Epoxy( request ).single( Page, {'id':page_id} ).json()

def page_by_slug( request, page_slug, page_language ):
	return Epoxy( request ).single( Page, {'slug':page_slug,'language':page_language} ).json()

def pin( request, page_id ):
	return Epoxy( request ).single( Pin, {'id':pin_id} ).json()

def pin_by_slug( request, pin_slug, pin_language ):
	return Epoxy( request ).single( Pin, {'slug':pin_slug,'language':pin_language} ).json()