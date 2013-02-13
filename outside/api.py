# -*- coding: utf-8 -*-



from django.db import IntegrityError 
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.conf import settings
from glue.models import Pin
from glue.misc import Epoxy, API_EXCEPTION_FORMERRORS, API_EXCEPTION_INTEGRITY
from outside.models import Subscriber, Message
from outside.forms import SubscriberForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, logout, authenticate
from outside.forms import LoginForm
from django.contrib.auth import login, logout, authenticate

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.contrib.sites.models import get_current_site
from django.utils.translation import ugettext as _



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
				description = form.cleaned_data['description'])
			s.save()

		except IntegrityError, e:
			try:
				s = Subscriber.objects.get( email=form.cleaned_data['email']  )

			except Subscriber.DoesNotExist, e:
				return response.throw_error( error="%s" % e, code=API_EXCEPTION_INTEGRITY).json()	
			# return response.throw_error( error="%s" % e, code=API_EXCEPTION_INTEGRITY).json()
		m = s.messages.create(
			content=form.cleaned_data['description']
		)
			
		
		
		
		#Notification mail to the client
		subject, from_email, to = _('Bequali : Message sent'),"L'équipe Bequali <admin@bequali.fr>", form.cleaned_data['email']
		text_content = '%s<br/><br/>%s</br>%s<br/><br/>%s<br/><br/>%s' % (_('Hello, your message has been sent, we will respond as soon as possible.'),
												_('Message content :'),
												form.cleaned_data['description'],
												_('Goodbye'),
												'<img src="http://quali.dime-shs.sciences-po.fr/bequali/static/img/bequali-logo.png"/>'
												)
				
		html_content = text_content.replace('\n', '<br/>')
		

		msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
		msg.attach_alternative(html_content, "text/html")
		msg.content_subtype = 'html'
		msg.send()
		
		
		
		form_datas2 = {'1. Prenom' : form.cleaned_data['first_name'],
				'2. nom' : form.cleaned_data['last_name'],
				'3. email' : form.cleaned_data['email'],
				'4. affiliation' : form.cleaned_data['affiliation'],
				'5. message' : form.cleaned_data['description']}	
		
		#Send mail to bequali admin : sarah.cadorel@sciences-po.fr, guillaume.garcia, anne.both
		subject, from_email, to = _('bequali contact request'),'admin@bequali.fr', settings.EMAIL_ADMINS
		html_content = '%s<br/><br/>%s<br/><br/>%s<br/><br/>%s</br/><br/>%s' % (
												_('Hello, you have a new contact request.'),
												_('Contact information :'), 
												''.join(['%s : %s<br/>' % (k, v) for k, v in sorted(form_datas2.items())]),
												_('Goodbye'),
												'<img src="http://quali.dime-shs.sciences-po.fr/bequali/static/img/bequali-logo.png"/>'
												)
		
		text_content = html_content.replace('<br/>', '\n')

											 
		msg2 = EmailMultiAlternatives(subject, text_content, from_email, to)
		msg2.attach_alternative(html_content, 'text/html')
		msg2.content_subtype = 'html'
		msg2.send()
		
		
		response.add("object", m, jsonify=True )

	return response.queryset( Subscriber.objects.filter() ).json()
	

def subscriber( request, subscriber_id ):
	return Epoxy( request ).single( Subscriber, {'id':subscriber_id} ).json()
	
@csrf_exempt
def login(request):
	logout(request)
	response = Epoxy(request)
	
	form = LoginForm( request.POST )
	if form.is_valid():
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
	else:
		return response.throw_error(error=form.errors, code=API_EXCEPTION_FORMERRORS ).json()
	
	if user is None:
		return response.throw_error(error="access denied" ).json()
	
	return response.json()

