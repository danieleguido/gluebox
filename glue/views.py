from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def index(request):
	data = _shared( request )
	return render_to_response('glue/index.html', RequestContext(request, data))

def _shared( request ):
	return {}