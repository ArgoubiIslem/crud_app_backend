from django.urls import path
from ProduitApp import views


urlpatterns = [
    path('produit/', views.produitApi),
    path('produit/<int:id>/', views.produitApi),

]
