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
        
        serializer = self.serializer_class(data=request.data)
      
        if serializer.is_valid():
             serializer.save()
             return Response({'message': 'el producto fue creado con exito'},status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # este return seria como el else del if de arriba
   
   
class ProductRetrieveAPIView(generics.RetrieveAPIView): # para listar o traer un producto especifico y desde la url o navegador le paso el id
     
     serializer_class=ProductSerializer
     
     
     def get_queryset(self):
          return self.get_serializer().Meta.model.objects.filter(state=True)# para listar o mostrar un solo producto se debe poner una consulta
     
     
     
class ProductDestroyAPIView(generics.DestroyAPIView):# para eliminar un producto
     
     serializer_class=ProductSerializer
     
     
     def get_queryset(self):
          return self.get_serializer().Meta.model.objects.filter(state=True)# para eliminar un producto se debe poner una consulta
     
     
     
     def delete(self, request, pk=None): # una forma de eliminar un producto pero no de la bbdd sino ocultandolo poniendo state=False
          # aca no uso el metodo updated ya que cambio es estado de state a False, porque si uso updated no me va a permitir hacer esta validacion paso a paso
          product =self.get_queryset().filter(id=pk).first()
          
          if product: # si esta el producto
             product.state=False
             product.save()
             
             return Response({'message': 'Producto eliminado correctamente'},status=status.HTTP_201_CREATED)
        
          return Response({'error': 'no existe un producto con estos datos'}, status=status.HTTP_400_BAD_REQUEST)# esto seria como el else del if de arriba que dice si hay producto
     
  