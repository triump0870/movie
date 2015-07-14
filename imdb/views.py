from imdb.models import Movie
from imdb.serializers import MovieSerializer, UserSerializer
from imdb.permissions import IsOwnerOrReadOnly
from imdb.forms import MovieFilter

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
	This endpoint presents the users in the system.
	As you can see, the collection of movie instances owned by a user are
	serialized using a hyperlinked representation.
	"""

	queryset = User.objects.all()
	serializer_class = UserSerializer

class MovieViewSet(viewsets.ModelViewSet):
	"""
	This endpoint presents movie instances.

    The `trailer` field presents a hyperlink to the trailer page which is a
    HTMLrepresentation of the youtube trailer.

    The **owner** of the movie may update or delete instances
    of the movie.
	"""
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
	filter_class = MovieFilter
	search_field = ('name', 'directorName','genre',)
	ordering_field = ('releaseDate', 'name',)

	@detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
	def trailer(self, request, *args, **kwargs):
		movie = self.get_object()
		return Response(
			movie.name
			)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)