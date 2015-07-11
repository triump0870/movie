# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt

# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response 
from rest_framework import status

from snippet.models import Snippet
from snippet.serializers import SnippetSerializer

# Create your views here.

# class JSONResponse(HttpResponse):
# 	"""
# 	An HttpResponse that renders its content into JSON.
# 	"""
# 	def __init__(self, data, **kwargs):
# 		content = JSONRenderer().render(data)
# 		kwargs['content_type'] = 'application/json'
# 		super(JSONResponse, self).__init__(content, **kwargs)

@api_view(['GET', 'POST'])
# @permission_classes((permissions.AllowAny,))
def snippet_list(request, format=None):
	"""
	List all snippets, or create a new snippet.
	"""
	if request.method == 'GET':
		snippets = Snippet.objects.all()
		serializer = SnippetSerializer(snippets, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = SnippetSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @csrf_exempt
# def snippet_list(request):
# 	"""
# 	List all code snippets, or create a new snippet.
# 	"""
# 	if request.method == 'GET':
# 		snippets = Snippet.objects.all()
# 		serializer = SnippetSerializer(snippets, many=True)
# 		return JSONResponse(serializer.data)

# 	elif request.method == 'POST':
# 		data = JSONParser().parse(request)
# 		serializer = SnippetSerializer(data=data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return JSONResponse(serializer.data, status=201)
# 		return JSONResponse(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes((permissions.AllowAny,))
def snippet_detail(request, pk, format=None):
	"""
	Retrieve, update or delete a code snippet.
	"""
	try:
		snippet = Snippet.objects.get(pk=pk)
	except Snippet.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = SnippetSerializer(snippet)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = SnippetSerializer(snippet, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		snippet.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

