from django import forms
from .models import AnimeList
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AnimeForm(forms.ModelForm):
    class Meta:
        model=AnimeList
        fields=[
            'name',
            'genre',
            'discription',
            'next_episode',
        ]