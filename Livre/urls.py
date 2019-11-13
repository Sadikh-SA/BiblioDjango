from django.urls import path
from . import views
# from Bibliotheque.settings import DEBUG
# from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name = 'index'),
    path('ajouter/', views.ajouter, name='ajouter'),
    path('modifier/<int:livre_id>', views.modifier_livre),
    path('supprimer/<int:livre_id>', views.supprimer_livre)
]
#DataFlair
