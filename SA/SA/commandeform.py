from socket import fromshare
from django import forms

JOBS=(
    ("python","Laptop"),
    ("javaScript","Destock"),
    ("csharp","Airpod"),
    ("cshap","Alibaba"),

)


class commande(forms.Form):
    produit=forms.ChoiceField(choices=JOBS, widget=forms.RadioSelect)
    Quantite=forms.FileField()
    specificite=forms.CharField(max_length=20, min_length=1)



from commande.models import mode

class modeform(forms.ModelForm):
    class Meta:
        model = mode
        fields = "__all__"

