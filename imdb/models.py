from django.db import models
# Create your models here.
class Genre(models.Model):
	"""Genre objects"""
	title = models.CharField(max_length=30)

	def __unicode__(self):
		return u'%s'%(self.title)

# class Director(models.Model):
# 	"""
# 	It holds the director informations.
# 	"""
# 	name = models.CharField(max_length=40)

# 	def __unicode__(self):
# 		# return u'%s'%(self.name)
# 		return self.name
		
class Movie(models.Model):
	"""Movie objects"""
	name = models.CharField(max_length=128)
	directorName = models.CharField(max_length=140, blank=False, null=False)
	genre = models.ManyToManyField(Genre)
	imdbScore = models.DecimalField(max_digits=2, decimal_places=1)
	popularity = models.DecimalField(max_digits=3, decimal_places=1)
	releaseDate = models.DateField(editable=True)
	owner = models.ForeignKey('auth.User', related_name='movies')
	
	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return ('movie_instance',(),{'pk':self.pk})