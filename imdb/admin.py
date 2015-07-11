from django.contrib import admin
from imdb import models

# Register your models here.


admin.site.register(models.Genre)
# class DirectorAdmin(admin.ModelAdmin):
# 	"""
# 	Admin model for Direcctor objects.
# 	"""
# 	list_display = ['name','movies']
# 	list_display_links = ['name']
# 	list_filter = ['name','movies']

admin.site.register(models.Director)

# class MovieAdmin(admin.ModelAdmin):
# 	"""
# 	Model Admin for Movie objects.
# 	"""
# 	list_display = ['name','director','imdb_score','created']
admin.site.register(models.Movie)