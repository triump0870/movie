from django.contrib.auth.models import User
from django.utils import six
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _ # To make the error message translatable

from rest_framework import serializers

from .models import Movie, Genre

# serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
	"""
	API serializer for Users.
	"""
	movies = serializers.HyperlinkedRelatedField(queryset=Movie.objects.all(), view_name='movie-detail', many=True)
	class Meta:
		model = User
		fields = ('url', 'username', 'movies')

class MovieSerializer(serializers.HyperlinkedModelSerializer):
	"""
	API serializer for Movie.
	"""
	owner = serializers.ReadOnlyField(source='owner.username')
	trailer = serializers.HyperlinkedIdentityField(view_name='movie-trailer', format='html')
	genre = serializers.SlugRelatedField(queryset=Genre.objects.all(), slug_field='title', many=True)

	class Meta:
		model = Movie
		fields = ('url','name','directorName', 'genre','trailer','imdbScore','popularity','releaseDate','owner')