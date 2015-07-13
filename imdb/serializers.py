from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Movie, Genre
from django.utils import six
import uuid
# serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups', 'is_staff')

# # serializer for user Group
# class GroupSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = Group
# 		fields = ('url', 'name')

class MyPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
	"""
	Overrides to_representation() method.
	"""
	# def __init__(self, **kwargs):
	# 	self.to_field = kwargs.pop('to_field',None)
	# 	super(MyPrimaryKeyRelatedField, self).__init__(**kwargs)

	# def use_pk_only_optimazation(self):
	# 	return False

	# def to_insternal_value(self, data):
	# 	try:
	# 		return self.get_queryset().get(**{self.to_field:data})
	# 	except ObjectDoesNotExist:
	# 		self.fail('does_not_exist', pk_value=data)
	# 	except (TypeError, ValueError):
	# 		self.fail('incorrect_type', data_type=type(data).__name__)
	# pass
	# def field_from_native(self, data, files, field_name, into):
	# 	data = dict(data)
	# 	print data
	# 	if self.many:
	# 		if data.get(field_name) == [u'null']:
	# 			data[field_name] = []
	# 	super(MyPrimaryKeyRelatedField, self).field_from_native(data, files, field_name, into)

	def to_representation(self, value):
		print "__________"
		print value
		print "--------------"
		return str(value) # Now returns the string representation instead of pk

class MovieSerializer(serializers.ModelSerializer):
	"""
	Serialiazing all the Movies.
	"""
	genre = MyPrimaryKeyRelatedField(many=True, queryset=Genre.objects.all())
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = Movie
		fields = ('popularity','directorName', 'genre','imdbScore','name','releaseDate','owner')

class NewMovieSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	movielist = serializers.HyperlinkedIdentityField(view_name='movie-highlight', format='html')

	class Meta:
		model = Movie
		fields = ('url', 'movielist','name', 'directorName', 'genre', 'popularity', 'imdbScore','owner')


