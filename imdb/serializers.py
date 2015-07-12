# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Movie, Genre
from django.utils import six
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

class MyPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
	"""
	Overrides to_representation() method.
	"""

	def to_representation(self, value):
		return str(value) # Now returns the string representation instead of pk

class MovieSerializer(serializers.ModelSerializer):
	"""
	Serialiazing all the Movies.
	"""
	genre = MyPrimaryKeyRelatedField(many=True, queryset=Genre.objects.all())
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = Movie
		fields = ('popularity','directorName', 'genre','imdbScore','name','owner')