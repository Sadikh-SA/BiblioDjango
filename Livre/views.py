from django.shortcuts import render, redirect
from .models import Livre
from .forms import CreerLivre
from django.http import HttpResponse

# Create your views here.
#CECI EST LA FONCTION POUR LISTER
def index(request):
    lister_livre = Livre.objects.all()
    return render(request, 'librairie.html', {'lister_livre': lister_livre})

#CECI EST LA FONCTION POUR AJOUTER
def ajouter(request):
    ajouter = CreerLivre()
    if request.method == 'POST':
        ajouter =  CreerLivre(request.POST, request.FILES)
        if ajouter.is_valid():
            ajouter.save()
            return redirect('index')
        else:
            return HttpResponse(""" Ton formulaire n'est pas valide Recharger <a href="{{url: 'index'}}">CHARGER</a> """)
    else:
        return render(request, 'upload_form.html', {'upload_form':ajouter})

#CECI EST LA FONCTION POUR MISE À JOUR
def modifier_livre(request, livre_id):
    id_livre = int(livre_id)
    try:
        livre_set = Livre.objects.get(id = id_livre)
    except Livre.DoesNotExist:
        return redirect('index')
    livre_form = CreerLivre(request.POST or None, instance = livre_set)
    if livre_form.is_valid():
        livre_form.save()
        return redirect('index')
    return render(request, 'upload_form.html', {'upload_form':livre_form})


#CECI EST LA FONCTION POUR SUPPRIMER
def supprimer_livre(request, livre_id):
    livre_id = int(livre_id)
    try:
        livre_set = Livre.objects.get(id = livre_id)
    except Livre.DoesNotExist:
        return redirect('index')
    livre_set.delete()
    return redirect('index')

