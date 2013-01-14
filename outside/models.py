from django.db import models
from django.contrib.auth.models import User


# a profile for the given user
class Subscriber( models.Model ):
	user = models.OneToOneField( User )
	first_name = models.CharField( max_length = 64 ) # longest than standard field
	last_name = models.CharField( max_length = 64 ) # longest than standard field
	email = models.EmailField()
	affiliation = models.CharField( max_length = 128 )
	accepted_terms = models.BooleanField()
	description = models.TextField() # personal description
