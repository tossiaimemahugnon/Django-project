from django.shortcuts import render

# Create your views here.
from SA.forms import signupForms

form=signupForms()
def formulaire(request):
    return render(request, 'signup.html',{"form":form})