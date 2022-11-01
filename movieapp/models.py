from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField()
    image = models.ImageField(upload_to='photos')

    def __str__(self):
        return self.name
