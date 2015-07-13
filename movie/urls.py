"""movie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
# from imdb.views import UserViewSet, GroupViewSet
from rest_framework import routers
import settings
from imdb import views
from django.views.generic import TemplateView
# Routers provide an easy way of automatically determining the URL conf
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'groups', GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^users/', views.UserViewSet.as_view(), name='users-list'),
    url(r'^movies/',include("imdb.urls")),
    # url(r'^$', template_name),
    # url(r'^',include(router.urls)),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="home"),

    # Login and Logout views for our api
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^snippets/', include("snippet.urls", namespace="snippet")),
    
]
# if settings.DEBUG:
#     urlpatterns += url(
#         r'^$', 'django.contrib.staticfiles.views.serve', kwargs={
#             'path': 'templates/index.html', 'document_root': settings.STATIC_ROOT}),