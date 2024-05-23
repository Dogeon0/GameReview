from django.conf import settings
from django.db import models
from datetime import date
def get_ratings():
    return [(int(key), value) for key, value in settings.RATINGS.items()]

class GameReview(models.Model):
    titulo = models.CharField(max_length=60)
    subtitlo = models.CharField(max_length=60)
    review = models.TextField(max_length=2000)
    autor = models.CharField(max_length=60)
    imagen = models.ImageField()
    rating = models.IntegerField(choices=get_ratings(),default=1)
    fecha = models.DateField(default=date.today)

