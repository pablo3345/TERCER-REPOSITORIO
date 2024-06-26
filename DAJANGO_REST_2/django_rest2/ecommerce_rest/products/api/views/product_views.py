from rest_framework import generics #esta libreria se coloca primero
from base.api import GeneralListApiView #GeneralListApiView seria como una vista de la app base
from products.api.serializers.product_serializers import ProductSerializer

from rest_framework.response import Response
from rest_framework import status

class ProductListAPIViews(GeneralListApiView):# la clase para listar los productos, parece que aca hereda de la vista de la app base GeneralListApiView para mostrar o listar los productos
    
     serializer_class = ProductSerializer
     
     
     
     
class ProductCreateAPIView(generics.CreateAPIView): # vista para crear un producto
     
     serializer_class= ProductSerializer # con esta sola linea de codigo ya me creo el producto con serializer_class= ProductSerializer
  #------------------------------------------------------------------------------   
     def post(self,request): # hago este metodo para personalizarlo, osea para poner mensajes al crear, para que sea mas entendible etc etc
          # em este caso el metodo get a igual que el metodo create sirven para guardar, crear
          
        serializer = self.serializer_class(data=request.data)
      
        if serializer.is_valid():
             serializer.save()
             return Response({'message': 'el producto fue creado con exito'},status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # este return seria como el else del if de arriba
     
     
  