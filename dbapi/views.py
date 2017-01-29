# coding=utf8

from django.shortcuts import render

# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from models import DrMas
from serializers import DrMasSerializer

# class JSONResponse(HttpResponse):
	# """
	# An HttpResponse that renders its content into JSON.
	# """
	# def __init__(self, data, **kwargs):
	# 	content = JSONRenderer().render(data)
	# 	kwargs['content_type'] = 'application/json'
	# 	super(JSONResponse, self).__init__(content, **kwargs)

@api_view(['GET', 'POST'])
def dr_list(request, format=None):
	if request.method == 'GET':
		snippets = DrMas.objects.all()
		serializer = DrMasSerializer(snippets, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = DrMasSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def dr_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = DrMas.objects.get(drCode=pk)
    except DrMas.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DrMasSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DrMasSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
