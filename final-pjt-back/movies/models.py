from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)


class Movie(models.Model) :
    movie_id = models.IntegerField()
    title = models.CharField(max_length=100)
    released_date = models.DateField()
    popularity = models.FloatField()
    vote_avg = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=500)
    genres = models.ManyToManyField(Genre)
    youtube_id = models.CharField(max_length=500)
    related_picture_path = models.CharField(max_length=500)
    logo_path = models.CharField(max_length=500)

class Latest(models.Model) :
    movie_id = models.IntegerField()
    title = models.CharField(max_length=100)
    released_date = models.DateField()
    genres = models.ManyToManyField(Genre)
    youtube_id = models.CharField(max_length=500)



class MovieComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    vote_rate = models.FloatField(default=0, validators=[MinValueValidator(0.5), MaxValueValidator(5.0)])
    created_at = models.DateTimeField(auto_now_add=True)


class UserGenre(models.Model):
    genres = models.ManyToManyField(Genre)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)