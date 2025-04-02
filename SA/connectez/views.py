from django.shortcuts import render

# Create your views here.
def connectez(request):
    return render(request,('connectez.html'))
