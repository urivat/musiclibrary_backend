from django.db import models

from like_songs.models import LikeSong

# Create your models here.
class Music_library(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    release_date = models.DateField()
    genre = models.CharField(max_length=255)
    like_status = models.ForeignKey(LikeSong)