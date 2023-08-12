from rest_framework import serializers
from ProduitApp.models import produit


class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = produit
        fields = ('id', 'nom', 'prix', 'quantite')
