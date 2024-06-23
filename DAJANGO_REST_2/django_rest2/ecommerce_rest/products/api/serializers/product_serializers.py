
from products.models import  Product
from rest_framework import serializers

# aqui vamos a tener todos los serializadores aplicables al producto (Product), aqui vamos a tener todos los serializadores que dependan del modelo Product

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
     model = Product
     
     exclude=('state',)