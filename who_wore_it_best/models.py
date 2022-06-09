from django.db import models
from django.urls import reverse

# Create your models here.
class PeopleVote(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    vote = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.name} | {self.vote}"

    def get_absolute_url(self):
        return reverse('who_wore_it_best:thanks')    