from django.contrib import admin

# Register your models here.
from django.contrib import admin
from who_wore_it_best.models import PeopleVote

admin.site.register(PeopleVote)