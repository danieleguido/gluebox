import json, os, inspect

from django.db.models.query import QuerySet, RawQuerySet
from django.conf import settings
from django.http import HttpResponse, HttpRequest
from django.forms import Form, IntegerField
#
#    CONSTS
#    ======
#

API_DEFAULT_OFFSET = 0
API_DEFAULT_LIMIT = 50
API_AVAILABLE_METHODS = [ 'DELETE', 'POST', 'GET' ]
API_EXCEPTION				=	'GenericException'
API_EXCEPTION_DOESNOTEXIST	=	'DoesNotExist'
API_EXCEPTION_DUPLICATED	=	'Duplicated'
API_EXCEPTION_FORMERRORS	=	'FormErrors'
API_EXCEPTION_INCOMPLETE	=	'Incomplete'
API_EXCEPTION_EMPTY			=	'Empty'
API_EXCEPTION_INVALID		=	'Invalid'

#
#    MISC FUNCTIONS
#    ==============
#

def whosdaddy( level=2 ):
	return inspect.stack()[level][3]


#
#    CLASSES
#    =======
#

class OffsetLimitForm( Form ):
	offset	= IntegerField( min_value=0, required=False, initial=0 )
	limit	= IntegerField( min_value=1, max_value=100, required=False, initial=25 )


class Epoxy:
	"""
	Understand requet.REQUEST meta params like django filters, limit/offset

	Usage:
	
	queryset = <Model>.objects.filter( **kwargs )
	return Epoxy( request ).get_response( queryset=queryset )

	"""
	def __init__(self, request ):
		self.request = request.REQUEST
		self.response = { 'status':'ok' } # a ditionary of things
		self.filters = {}
		self.method = ''
		self.limit = API_DEFAULT_LIMIT
		self.offset = API_DEFAULT_OFFSET
		self._process()

	def _process( self ):
		self.response['meta'] = {}
		self.response['meta']['action'] = whosdaddy(3)

		# understand method via REQUEST params

		# limit / offset 
		if self.method=='GET':
			if self.request.has_key('offset') or self.request.has_key('limit') :
				form = OffsetLimitForm( self.request )
				if form.is_valid():
					self.offset = form.cleaned_data['offset'] if form.cleaned_data['offset'] else self.offset 
					self.limit	= form.cleaned_data['limit'] if form.cleaned_data['limit'] else self.limit 
				else:
					self.response['meta']['warnings'] = form.errors
			self.response['meta']['offset'] = self.offset
			self.response['meta']['limit'] = self.limit

	def json( self, mimetype="application/json" ):
		if self.request is not None and self.request.has_key('indent'):
			return HttpResponse( json.dumps( self.response, indent=4),  mimetype=mimetype)
		return HttpResponse( json.dumps( self.response ), mimetype=mimetype)

	def response( self ):
		return self.response

	def throw_error( self, error="", code=API_EXCEPTION ):
		self.response[ 'status' ] = 'error'
		self.response[ 'error' ] = error
		self.response[ 'code' ] = code
		return self.json()

