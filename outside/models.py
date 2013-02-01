#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Message( models.Model ):
	date = models.DateField( auto_now=True )
	content = models.CharField( max_length = 1000 )

	def __unicode__(self):
		return "%s : %s" % ( self.date, self.content )

	def json( self ):
		return {
			'id': self.id,
			'content':self.content,
			'date' : self.date.isoformat()
		}

# a profile for the given user
class Subscriber( models.Model ):

	RESEARCHER = 'RES'
	PHD_STUDENT = 'PHD'
	MS_STUDENT = 'MSS'
	PROFESSOR = 'PRO'

	ENGINEEER = 'ENG'
	POST_DOC = 'POD'
	OTHER = 'OTH'

	STATUS_CHOICES = (
		(RESEARCHER, 'Chercheur Statutaire'),
		(PHD_STUDENT, 'Doctorant'),
		(MS_STUDENT, 'Étudiant - Master'),
		(PROFESSOR, 'Enseignant-Chercheur'),

		(ENGINEEER, 'Ingénieur'),
		(POST_DOC, 'Post Doc'),
		(OTHER, 'Autre'),
	)



	user = models.OneToOneField( User, null=True, blank=True )
	first_name = models.CharField( max_length = 64 ) # longest than standard field
	last_name = models.CharField( max_length = 64 ) # longest than standard field
	email = models.EmailField( unique=True )
	affiliation = models.CharField( max_length = 128 )
	status =     models.CharField( max_length = 3, choices=STATUS_CHOICES )
	accepted_terms = models.BooleanField()
	description = models.TextField() # personal description
	messages = models.ManyToManyField( Message )
	
	def __unicode__(self):
		return "%s %s <%s>" % (self.last_name.upper(), self.first_name, self.email )

	def json( self ):
		return {
			'id': self.id,
			'user':self.user,
			'first_name' : self.first_name,
			'last_name':self.last_name,
			'email' : self.email,
			'affiliation' : self.affiliation,
			'accepted_terms' : self.accepted_terms,
			'description' : self.description,
		}



