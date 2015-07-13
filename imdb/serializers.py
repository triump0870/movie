from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Movie, Genre
from django.utils import six
from django.core.exceptions import ObjectDoesNotExist
# serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
	movies = serializers.HyperlinkedRelatedField(queryset=Movie.objects.all(), view_name='movie-detail', many=True)
	class Meta:
		model = User
		fields = ('url', 'username', 'movies')

class MyPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
	"""
	Overrides to_representation() method.
	"""
	def to_representation(self, value):
		return six.text_type(value) # Now returns the string representation instead of pk

class MovieSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	trailer = serializers.HyperlinkedIdentityField(view_name='movie-trailer', format='html')
	genre = MyPrimaryKeyRelatedField(many=True, queryset=Genre.objects.all())

	class Meta:
		model = Movie
		fields = ('url','name','directorName', 'genre','trailer','imdbScore','popularity','releaseDate','owner')


