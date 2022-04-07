from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from music import serializer
from music.models import Music_library
from music.serializer import MusicSerializer
# Create your views here.
class LibraryList(APIView):
    def get(self,request, format=None):
        music_query = Music_library.objects.all()
        serializer= MusicSerializer(music_query, many=True)
        return Response(serializer.data)
    