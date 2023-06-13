from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
    phone_number = models.IntegerField()
    bio = models.TextField()
    image_id = models.IntegerField()
