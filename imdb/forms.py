import django_filters

from .models import Movie

# Filter class
class MovieFilter(django_filters.FilterSet):
	class Meta:
		model = Movie
		fields = ('name', 'directorName', 'releaseDate')