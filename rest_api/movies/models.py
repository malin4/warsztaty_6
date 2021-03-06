from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=255)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    director = models.ForeignKey(Person, related_name="movie_director", on_delete=None)
    actors = models.ManyToManyField(Person, trought='MoviePerson'related_name="movies_cast")
    year = models.SmallIntegerField()
