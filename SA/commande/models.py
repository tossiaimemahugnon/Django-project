from django.db import models

# Create your models here.
class mode(models.Model):
    produit=models.CharField(max_length=200)
    quantite=models.SlugField
    specificite=models.TextField()
    date=models.DateField()
