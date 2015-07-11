# from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import TemplateView
from imdb.models import Movie
from imdb.serializers import MovieSerializer
from rest_framework import generics
from rest_framework import permissions
from imdb.permissions import IsOwnerOrReadOnly
# from rest_framework import viewsets
# from django.contrib.auth.models import User, Group
# from imdb.serializers import UserSerializer, GroupSerializer
# Create your views here.

class IndexView(generics.ListCreateAPIView):
	template_name = 'index.html'
	queryset = Movie.objects.all()		
	permissions_classes = (permissions.IsAuthenticatedOrReadOnly,)
	serializer_class = MovieSerializer

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
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

class MovieInstanceView(generics.RetrieveUpdateDestroyAPIView):
	"""
	Returns a single movie.
	Also allows updating and deleting
	"""
	queryset = Movie.objects.all()
	permissions_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
	serializer_class = MovieSerializer