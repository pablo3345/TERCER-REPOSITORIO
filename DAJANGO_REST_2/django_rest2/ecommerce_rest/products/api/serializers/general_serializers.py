from products.models import MeasureUnit, CategoryProduct, Indicator # estos son los modelos generales, aca no uso el modelo Product xq es un modelo principal
from rest_framework import serializers

class MeasureUnitSerializars(serializers.ModelSerializer):
    
    class Meta:
        model = MeasureUnit
        exclude=('state',) # xq excluimos el campo estado?, xq el campo estado se maneja de forma automatica, y solo se cambia cuando se desee en este caso, cuando se necesite eliminar de forma logica algun registro, en otro motivo el campo estado no se va a utilizar
        # no nos olvidemos que state viene del modelo Base que hereda
        
        
class CategoryProductSerializars(serializers.ModelSerializer):
    
      class Meta:
        model = CategoryProduct
        exclude=('state',)
    
    
class IndicatorSerializers(serializers.ModelSerializer):
    
      class Meta:
        model = Indicator
        exclude=('state',)
    