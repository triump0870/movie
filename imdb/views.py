# from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import TemplateView

from imdb.models import Movie
from imdb.serializers import MovieSerializer, NewMovieSerializer
from imdb.permissions import IsOwnerOrReadOnly

from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets

from django.contrib.auth.models import User
from imdb.serializers import UserSerializer
# Create your views here.

@api_view(('GET',))
def api_root(request, format=None):
	return Response({
		# 'users': reverse('user-list', request=request, format=format),
		'movies': reverse('movies-list', request=request, format=format),
		# 'movieList' : reverse('movie-instance', request=request, format=format),

		})
class IndexView(generics.ListCreateAPIView):
	template_name = 'index.html'
	queryset = Movie.objects.all()		
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
 	serializer_class = MovieSerializer
	renderers_classes = (renderers.StaticHTMLRenderer,)


	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoints that allows users to be viewed or edited.
	"""

	queryset = User.objects.all()
	serializer_class = UserSerializer

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

class MovieHighlight(generics.GenericAPIView):
	template_name = 'index.html'
	queryset = Movie.objects.all()
	renderers_classes = (renderers.StaticHTMLRenderer,)
	serializer_class = NewMovieSerializer

	def get(self, request, *args, **kwargs):
		movie = self.get_object()
		return Response({'name':movie.name, 'directorName':movie.directorName}, template_name='index.html')