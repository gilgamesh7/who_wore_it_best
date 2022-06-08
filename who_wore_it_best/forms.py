from tkinter import Button
from django import forms
from who_wore_it_best.models import PeopleVote

class VoteForm(forms.ModelForm):
    class Meta:
        model = PeopleVote
        fields = '__all__'

        widgets = {
            'name' : forms.Select(attrs={'class': 'form-control'}),
            'vote' : forms.CheckboxInput(attrs={'class': 'form-control'}),
        }