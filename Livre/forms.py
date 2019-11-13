from django import forms
from .models import Livre
# from django.db import models


class CreerLivre(forms.ModelForm):
    nom = forms.CharField(max_length = 50, help_text = "Enter un nom")
    photo = forms.ImageField()
    auteur = forms.CharField(max_length = 150)
    email = forms.EmailField()
    #description = forms.TextField(default = 'Tutoriel crud Django')
    class Meta:
        model: Livre
        fields: "__all__"