from django.db import models
from django.contrib.auth.models import User


# a profile for the given user
class Subscriber( models.Model ):

	PHD_STUDENT = 'PHD'
	PROFESSOR = 'PRO'

	STATUS_CHOICES = (
		(PHD_STUDENT, 'PHD Student'),
		(PROFESSOR, 'Professor')	
	)


	user = models.OneToOneField( User, null=True, blank=True )
	first_name = models.CharField( max_length = 64 ) # longest than standard field
	last_name = models.CharField( max_length = 64 ) # longest than standard field
	email = models.EmailField( unique=True )
	affiliation = models.CharField( max_length = 128 )
	status =     models.CharField( max_length = 3, choices=STATUS_CHOICES )
	accepted_terms = models.BooleanField()
	description = models.TextField() # personal description
	
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
