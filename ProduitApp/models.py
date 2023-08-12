from django.db import models

# Create your models here.


class produit(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=(500))
    prix = models.IntegerField()
    quantite = models.IntegerField()
