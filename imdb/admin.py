from django.contrib import admin
from imdb import models

# Register your models here.


admin.site.register(models.Genre)
# class DirectorAdmin(admin.ModelAdmin):
# 	"""
# 	Admin model for Direcctor objects.
# 	"""
# 	# list_display = ['name']
# 	# list_display_links = ['name']
# 	list_filter = ['name']

# admin.site.register(models.Director, DirectorAdmin)

class MovieAdmin(admin.ModelAdmin):
	"""
	Model Admin for Movie objects.
	"""
	list_display = ['name','imdbScore', 'releaseDate']
	list_display_links = ['name']
	list_filter = ['name','releaseDate']

admin.site.register(models.Movie, MovieAdmin)