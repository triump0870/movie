from django.conf.urls import patterns, url
from imdb import views

urlpatterns = patterns('',
	url(r'^$',views.IndexView.as_view(), name='movie_list'),
	url(r'^(?P<pk>[\d]+)/$', views.MovieInstanceView.as_view(), name='movie_instance'),
	)