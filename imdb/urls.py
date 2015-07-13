from django.conf.urls import patterns, url
from imdb import views

urlpatterns = patterns('',
	# url(r'^$',views.api_root, name='movies-list'),
	# url(r'^)
	url(r'^$', views.IndexView.as_view(), name='movies-list'),
	url(r'^(?P<pk>[\d]+)/$', views.MovieInstanceView.as_view(), name='movie-instance'),
	url(r'^(?P<pk>[0-9]+)/highlight/$', views.MovieHighlight.as_view(), name='movie-highlight'),
	
	)