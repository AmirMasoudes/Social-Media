from django.db import models

# Create your models here.

class comment(models.Model):
    user_id = models.IntegerField()
    comment = models.TextField()
    like_id = models.IntegerField()
    reply = models.TextField()
# rep