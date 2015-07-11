# from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import TemplateView
from imdb.models import Movie
from imdb.serializers import MovieSerializer
from rest_framework import generics

# from rest_framework import viewsets
# from django.contrib.auth.models import User, Group
# from imdb.serializers import UserSerializer, GroupSerializer
# Create your views here.

class IndexView(generics.ListAPIView):
	# template_name = 'index.html'
	queryset = Movie.objects.all()
	model = Movie
	serializer_class = MovieSerializer

# class UserViewSet(viewsets.ModelViewSet):
# 	"""
# 	API endpoints that allows users to be viewed or edited.
# 	"""

# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer

# class GroupViewSet(viewsets.ModelViewSet):
# 	"""
# 	API endpoints that allows groups to be viewed or edited.
# 	"""
	
# 	queryset = Group.objects.all()
# 	serializer_class = GroupSerializer