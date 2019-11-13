from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Livre(models.Model):
    nom = models.CharField(max_length = 50)
    photo = models.ImageField()
    auteur = models.CharField(max_length = 150, default = 'Tester')
    email = models.EmailField(blank = True)
    description = models.TextField(default = 'Tutoriel crud Django')
    def __str__(self):
        return self.nom

