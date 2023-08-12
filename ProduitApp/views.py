from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from ProduitApp.models import produit
from ProduitApp.serializers import ProduitSerializer
# Create your views here.


@csrf_exempt
def produitApi(request, id=0):
    if request.method == 'GET':
        produits = produit.objects.all()
        produits_serializer = ProduitSerializer(produits, many=True)
        return JsonResponse(produits_serializer.data, safe=False)
    elif request.method == 'POST':
        produit_data = JSONParser().parse(request)
        produits_serializer = ProduitSerializer(data=produit_data)
        if produits_serializer .is_valid():
            produits_serializer .save()
            return JsonResponse("Enregistrer avec succer", safe=False)
        return JsonResponse("erreur d'enregistrement", safe=False)
    elif request.method == 'PUT':
        produit_data = JSONParser().parse(request)
        produite = produit.objects.get(id=produit_data['id'])
        produits_serializer = ProduitSerializer(produite, data=produit_data)
        if produits_serializer .is_valid():
            produits_serializer .save()
            return JsonResponse("Modification avec succer", safe=False)
        return JsonResponse("erreur de modification", safe=False)
    elif request.method == 'DELETE':
        produite = produit.objects.get(id=id)
        produite.delete()
        return JsonResponse("supprission avec succer", safe=False)
    return JsonResponse("erreur de supprission", safe=False)
