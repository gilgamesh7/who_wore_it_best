# Generated by Django 4.0.5 on 2022-06-05 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('who_wore_it_best', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='people_vote',
            new_name='PeopleVote',
        ),
    ]
