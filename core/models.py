from django.db import models

# Create your models here.

class image(models.Model):
    image = models.ImageField()




class like(models.Model):
    user_id = models.IntegerField()
