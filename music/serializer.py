import music
from music.models import Music_library
from rest_framework import serializers

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music_library
        fields = ['id' , 'title', 'artist','album','release_date', 'genre']