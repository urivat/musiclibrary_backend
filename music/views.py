from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from music.serializer import MusicSerializer
# Create your views here.
class LibraryDetails(APIView):
    def get(self,request, format=None):
        return Response('hello')