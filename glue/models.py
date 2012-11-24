from django.db import models

LANGUAGE_CHOICES = (
	('EN', 'EN'),
	('FR', 'FR')
)

class Geo( models.Model): # geo spot, with zoom
	lat = models.FloatField() # map center LAT
	lon = models.FloatField() # map center LON
	zoom = models.IntegerField() # start zoom
	content = models.TextField( default="", blank=True, null=True ) # textual GEO description
	
class Pin( models.Model ):
	slug = models.SlugField()
	title = models.CharField( max_length=160, default="", blank=True, null=True )
	abstract = models.TextField( default="", blank=True, null=True )
	content = models.TextField( default="", blank=True, null=True )
	language =  models.CharField( max_length=2, default='EN', choices=LANGUAGE_CHOICES ) # magic admin features: create a pin for the same language
	
	mimetype = models.CharField( max_length=255, default="", blank=True, null=True )
	sort =  models.IntegerField( default=0 )

	date = models.DateField( blank=True, null=True ) # main date, manually added 
	date_last_modified = models.DateField( auto_now=True ) # date last save()
	
	local = models.FileField( upload_to='pins/%Y-%m/',  blank=True, null=True ) # local stored file
	permalink  = models.TextField( default="", blank=True, null=True ) # remote link

	related = models.ManyToManyField("self", symmetrical=True, null=True, blank=True)
	geos = models.ManyToManyField( Geo, blank=True, null=True ) # add geographic point

	class Meta:
		unique_together = ( "slug", "language" )

	def json( self, recursive=True ):
		return{
			'id': self.id,
			'slug':self.slug,
			'title': self.title,
			'abstract': self.abstract,
			'content': self.content,
			'language': self.language,
			'mimetype': self.mimetype,
			'related': [ p.json( recursive=False) for p in self.related.all() ] if recursive else self.related.count()
		}


class Page( models.Model ):
	slug = models.SlugField()
	title = models.CharField( max_length=160, default="", blank=True, null=True )
	abstract = models.TextField( default="", blank=True, null=True )
	content = models.TextField( default="", blank=True, null=True )
	
	language =  models.CharField( max_length=2, default='EN', choices=LANGUAGE_CHOICES ) # magic admin features: create a pin for the same language
	
	pins = models.ManyToManyField( Pin, null=True, blank=True)

	class Meta:
		unique_together = ( "slug", "language" )

	def json( self ):
		return{
			'id': self.id,
			'slug':self.slug,
			'title': self.title,
			'abstract': self.abstract,
			'content': self.content,
			'language': self.language
		}