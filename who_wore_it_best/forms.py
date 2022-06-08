from tkinter import Button
from django import forms
from who_wore_it_best.models import PeopleVote

people = [
    ('', ''),
    ('Dee', 'Dee Williamson'),
    ('Tony', 'Anthony Bus'),
    ('Roopal', 'Roopal Vishwakarma'),
    ('Srikar', 'Srikar vangala')
]

votes = [
    ('', ''),
    ('Rajesh', 'Rajesh'),
    ('Naresh', 'Naresh'),
]
class VoteForm(forms.ModelForm):
    class Meta:
        model = PeopleVote
        fields = '__all__'

        # widgets = {
        #     'name' : forms.Select(attrs={'class': 'form-control'}, choices=people),
        #     'vote' : forms.Select(attrs={'class': 'form-control'}, choices=votes),
        # }
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'vote' : forms.TextInput(attrs={'class': 'form-control'}),
        }