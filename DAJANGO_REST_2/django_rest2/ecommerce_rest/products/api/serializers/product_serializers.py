from rest_framework import serializers
from products.models import  Product
from rest_framework import serializers
from products.api.serializers.general_serializers import MeasureUnitSerializars, CategoryProductSerializars



# aqui vamos a tener todos los serializadores aplicables al producto (Product), aqui vamos a tener todos los serializadores que dependan del modelo Product

class ProductSerializer(serializers.ModelSerializer):
  
    
    class Meta:
     model = Product
     
     exclude=('state',) # los campos que pongo aca en el field son los que se me van a ver en la interfaz swagger
     
      #----------para no mostrar el numero de foreign Key y si su nombre real-----------------------------
    
   # measure_unit=MeasureUnitSerializars() # el campo del modelo producto con su serializador
   # category_product =CategoryProductSerializars()# para que en el listado no me aparezca el numero de la foreign Key del modelo producto y si el nombre real de unidad de medida y categoria
   
    # debo poner el nombre aca igual que esta en el modelo producto para que me lo reconozca
    # otra forma de hacerlo es escribir category_product=serializers.StringRelatedField() y con esto me va a mostrar lo que tengo escrito en el __str__ del modelo producto
   # measure_unit=serializers.StringRelatedField() 
   # category_product = serializers.StringRelatedField()
    
    
    
    def to_representation(self, instance):# en este caso en especial esta es la forma correcta de mostrar el nombre real de la foreign Key y no el numero, ya que tiene una imagen como nula y hay que validarla xq puede generar error
      return {'id': instance.id,
              'name': instance.name,
              'description': instance.description,
              'image': instance.image if instance.image else None, # como la imagen es nula y me daba error puese esto para que me retorne un None si no pongo nada en el campo image, esto seria validar
              'measure_unit': instance.measure_unit.description  if instance.measure_unit != None else "", 
              'category_product': instance.category_product.description  if instance.category_product != None else "" } # para que me retorne una cadena vacia y no me de error cuando hago ciertos metodos en la interfaz de ayuda (esto seria una validacion)
    
    
    #---------------------------------------------------------------------------------------------------
    
  