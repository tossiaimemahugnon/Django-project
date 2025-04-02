from django.urls import path
from  django import urls
from . import views

urlpatterns = [
path ('commande/',views.commande),
path('modele/', views.ceform),
 ]
