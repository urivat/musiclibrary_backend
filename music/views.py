from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from music import serializer
from music.models import Music_library
from music.serializer import MusicSerializer
from rest_framework import status
from django.http import Http404
# Create your views here.
class LibraryList(APIView):
    def get(self,request, format=None):
        music_query = Music_library.objects.all()
        serializer= MusicSerializer(music_query, many=True)
        return Response(serializer.data)
    def post(self,request, format=None):
        serializer = MusicSerializer(data= request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
class LibraryDetails(APIView):
    def get_by_id(self, pk):
        try:
            return Music_library.objects.get(pk=pk)
        except Music_library.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        songs = self.get_by_id(pk)
        serializer= MusicSerializer(songs)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        songs= self.get_by_id(pk)
        serializer= MusicSerializer(songs, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        songs = self.get_by_id(pk)
        songs.delete()
        return Response(status=status.HTTP_200_OK)
        