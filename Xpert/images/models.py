from django.db import models

# Create your models here.
class Slider(models.Model):

    h3white = models.TextField()
    h1white = models.TextField()
    h1yellow = models.TextField()
    para = models.TextField()
    image = models.ImageField()

class Gallery(models.Model):

    image = models.ImageField()

class Service(models.Model):

    h3white = models.TextField()
    para = models.TextField()
    image = models.ImageField(upload_to='media')