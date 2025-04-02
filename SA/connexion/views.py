# connexion/views.py
from django.shortcuts import render
from django.http import HttpResponse

def connect(request):
    return render(request, 'connect.html')
