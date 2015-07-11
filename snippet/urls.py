from django.conf.urls import patterns, url 

from snippet import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	url(r'^$', views.snippet_list),
	url(r'^(?P<pk>[0-9]+)/$', views.snippet_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)