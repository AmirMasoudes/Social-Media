from django.db import models

# Create your models here.

class post(models.Model):
    image_id = models.IntegerField()
    user_id = models.IntegerField()
    description = models.IntegerField()
    comment_id = models.TextField()
    like_id = models.IntegerField()




