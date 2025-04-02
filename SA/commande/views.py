from django.shortcuts import render
from SA.commandeform import commande
form=commande()
def commande(request):
    #if request.method == "POST":
       # form=commande(request.POST)
        #if form.is_valid():
           # print(form.cleaned_data)
  #  else:
    
    return render(request, 'commandez.html', {"form":form})
from SA.commandeform import modeform
formu=modeform()
def ceform(request):
    return render(request,'tester.html', {"formu":formu})

