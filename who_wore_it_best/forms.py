from tkinter import Button
from django import forms
from who_wore_it_best.models import PeopleVote

people = [
    ('', ''),
    ('Dee Williamson', 'Dee Williamson'),
    ('Anthony Bus', 'Anthony Bus'),
    ('Roopal Vishwakarma', 'Roopal Vishwakarma'),
    ('Srikar Vangala', 'Srikar Vangala'),
    ('Vishaal Prasad', 'Vishaal Prasad'),
    ('Sudha Sachidanandam', 'Sudha Sachidanandam'),
    ('Stephen Gupwell', 'Stephen Gupwell'),
    ('Ramanjulu Sunkari', 'Ramanjulu Sunkari'),
    ('Rajesh Babu', 'Rajesh Babu'),
    ('Pawan Kumar', 'Pawan Kumar'),
    ('Norman Close', 'Norman Close'),
    ('Malishka Walpole Lokuge', 'Malishka Walpole Lokuge'),
    ('Sourav Shaw', 'Sourav Shaw'),
    ('Naresh Seth', 'Naresh Seth'),
    ('Mark Annas', 'Mark Annas'),
    ('Felix Lee', 'Felix Lee'),
    ('Bernard OLeary', 'Bernard OLeary'),
]

votes = [
    ('', ''),
    ('Rajesh', 'Rajesh'),
    ('Naresh', 'Naresh'),
]
class VoteForm(forms.ModelForm):
    class Meta:
        model = PeopleVote
        fields = ['name','vote']

        widgets = {
            'name' : forms.Select(attrs={'class': 'form-control'}, choices=people),
            'vote' : forms.Select(attrs={'class': 'form-control'}, choices=votes),
        }
        # widgets = {
        #     'name' : forms.TextInput(attrs={'class': 'form-control'}),
        #     'vote' : forms.Select(attrs={'class': 'form-control'}, choices=votes),
        # }