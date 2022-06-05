from django.db import models

# Create your models here.
class PeopleVote(models.Model):
    name = models.CharField(max_length=100)
    vote = models.CharField(max_length=100)