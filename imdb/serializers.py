# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Movie, Director
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
	class Meta:
		model = Movie
		fields = ('popularity','directorName','genre','imdbScore','name')

class DirectorSerializer(serializers.ModelSerializer):
	"""
	Serialiazing all the directors.
	"""
	class Meta:
		model = Director
		fields = ('name')