
#from rest_framework import generics # primero va esta libreria y luego las demas
#from products.models import MeasureUnit, CategoryProduct, Indicator
from products.api.serializers.general_serializers import MeasureUnitSerializars, CategoryProductSerializars,  IndicatorSerializers

from base.api import GeneralListApiView # aca importo la vista de base.api, me ahorro de escribir codigo en estas 3 vistas, xq hice una funcion general en api de la aplicacion base que reemplaza estas 3 vistas

#antes estas vistas heredaban de generics.ListAPIView, pero las hice generales desde la aplicacion base o padre que es la que heredan

class MeasureUnitListAPIView(GeneralListApiView): # es la clase generica que django rest framework tiene como objetivo netamente para listar, mostrar la informacion (ListAPIView)
   
   
    serializer_class = MeasureUnitSerializars # le enviamos al serializador, serializer_class este nombre no puede ser otro, es asi como esta
    
    #def get_queryset(self): # las funciones dentro de las clases de la vistas, parece que ya tienen nombres fijos que no se pueden modificar
   #  return MeasureUnit.objects.filter(state=True) #state=True simplemente para que no me muestre las eliminadas
    # aca ya tengo mi listado de MeasureUnit creadas, en formato json
    
    

class CategoryProductListAPIView(GeneralListApiView): 
   
    serializer_class = CategoryProductSerializars
    
   # def get_queryset(self):
    # return CategoryProduct.objects.filter(state=True)
  

class IndicadorListAPIView(GeneralListApiView): 
   
    serializer_class = IndicatorSerializers
    
   # def get_queryset(self):
   #  return Indicator.objects.filter(state=True)
  
