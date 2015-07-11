from django.forms import widgets
from rest_framework import serializers
from snippet.models import Snippet, LANGUAGE_CHOICE, STYLE_CHOICE

# class SnippetSerializer(serializers.Serializer):
# 	"""It provides Web API to serialize and deserialize the snippet
# 	instance into representation such as JSON."""

# 	pk = serializers.IntegerField(read_only=True)
# 	title = serializers.CharField(required=False, allow_blank=True, max_length=100)
# 	code = serializers.CharField(style={'base_template':'textarea.html'})
# 	linenos = serializers.BooleanField(required=False)
# 	language = serializers.ChoiceField(choices=LANGUAGE_CHOICE, default='python')
# 	style = serializers.ChoiceField(choices=STYLE_CHOICE, default='friendly')

# 	def create(self, validate_data):
# 		"""
# 		Create and return new `Snippet` instance, given the validated data.
# 		"""
# 		return Snippet.objects.create(**validate_data)

# 	def update(self, instance, validate_data):
# 		"""
# 		Update and return an existing `Snippet` instance, given the validated data.
# 		"""
# 		instance.title = validate_data.get('title', instance.title)
# 		instance.code = validate_data.get('code', instance.code)
# 		instance.linenos = validate_data.get('linenos', instance.linenos)
# 		instance.language = validate_data.get('language', instance.language)
# 		instance.style = validate_data.get('style', instance.style)
# 		instance.save()

# 		return instance

class SnippetSerializer(serializers.ModelSerializer):
	"""
	Refactoring the serializer using the ModelSerializer class.
	"""
	class Meta:
		model = Snippet
		fields = ('id', 'title', 'code', 'linenos', 'language', 'style')
		