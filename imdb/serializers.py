# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Movie, Director, Genre
# serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = User
# 		fields = ('url', 'username', 'email', 'groups', 'is_staff')

# # serializer for user Group
# class GroupSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = Group
# 		fields = ('url', 'name')

class MovieSerializer(serializers.ModelSerializer):
	"""
	Serialiazing all the Movies.
	"""
	# search_url = serializers.SerializerMethodField('get_search_url')
	genre = serializers.PrimaryKeyRelatedField(many=True, queryset=Genre.objects.all())
	directorName = serializers.PrimaryKeyRelatedField(queryset=Director.objects.all())
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = Movie
		fields = ('popularity',"directorName",'genre','imdbScore','name','owner')

	# def get_search_url(self, obj):
	# 	return 'http://www.imdb.com/title/{}'.format(obj.name)

class DirectorSerializer(serializers.ModelSerializer):
	"""
	Serialiazing all the directors.
	"""
	movies = serializers.PrimaryKeyRelatedField(many=True, queryset=Movie.objects.all())
	class Meta:
		model = Director
		fields = ('name','movies')
