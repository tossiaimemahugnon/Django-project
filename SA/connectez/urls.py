from django.urls import path
from . import views

urlpatterns = [
    path('connectez/', views.connectez),
]
