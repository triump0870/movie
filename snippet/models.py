from django.db import models

# Using pygments for the code highlighting
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# Global constants
LEXERS = [ item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICE = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICE = sorted((item, item) for item in get_all_styles())

# Create your models here.
class Snippet(models.Model):
	"""Snippet object --- used to store code snippet"""
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100, blank=True, default='')
	code = models.TextField()
	linenos = models.BooleanField(default=False)
	language = models.CharField(choices=LANGUAGE_CHOICE, default='python', max_length=100)
	style = models.CharField(choices=STYLE_CHOICE, default='friendly', max_length=100)

	class Meta:
		ordering = ('created',)