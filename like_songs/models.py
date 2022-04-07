from django.db import models

# Create your models here.
class LikeSong(models.Model):
    like= models.BooleanField()