from imdb.models import Movie
from imdb.serializers import MovieSerializer, UserSerializer
from imdb.permissions import IsOwnerOrReadOnly

from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import detail_route
from rest_framework.response import Response 
from rest_framework import renderers
from rest_framework import viewsets

from django.contrib.auth.models import User
# Create your views here.

class UserViewSet(viewsets.ReadOnlyModelViewSet):
	"""
	API endpoints that allows users to be viewed or edited.
	"""

	queryset = User.objects.all()
	serializer_class = UserSerializer

class MovieViewSet(viewsets.ModelViewSet):
	"""
	This viewset automatically provides `list`, `Create, `retrieve`,
	`update` and `destroy` actions.

	Additionally we also provide an extra `show` action.
	"""
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

	@detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
	def trailer(self, request, *args, **kwargs):
		movie = self.get_object()
		return Response(
			movie.name
			)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)