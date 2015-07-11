from django.db import models

# Create your models here.
class Genre(models.Model):
	"""Genre objects"""
	title = models.CharField(max_length=30)

	def __unicode__(self):
		return self.title

class Director(models.Model):
	"""
	It holds the director informations.
	"""
	name = models.CharField(max_length=40)
	movies = models.ForeignKey('Movie',blank=True, null=True)

	def __unicode__(self):
		return self.name

class Movie(models.Model):
	"""Movie objects"""
	name = models.CharField(max_length=128)
	directorName = models.ForeignKey(Director)
	genre = models.ManyToManyField(Genre)
	imdbScore = models.DecimalField(max_digits=2, decimal_places=1)
	popularity = models.DecimalField(max_digits=3, decimal_places=1)
	releaseDate = models.DateField(editable=True)

	def __unicode__(self):
		return self.name
