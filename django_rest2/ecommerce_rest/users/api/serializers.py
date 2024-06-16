# creamos un serielizador para nuestro modelo usuario
# un sereilizador es cuando toma los datos de un modelo para convertirlos en json, para retornar un json

from rest_framework import serializers
from users.models import User

# ahora creo el serializazors, que me convierte a json

class UserSerializer(serializers.ModelSerializer): # va a ser un serielizadors basado en un modelo, por eso hereda de ModelSerializer
    
     class Meta:
       model =User
       fields = '__all__'   # si quiero campos especificos, hago como en el fields del formModels de django
       
    
    

class TestUserSerializador(serializers.Serializer): # no tiene como parametro ModelSerializer xq un serializador no siempre esta basado en un modelo
  name = serializers.CharField(max_length=200)
  email = serializers.EmailField()
  
  def validate_name(self,value):
    
    print(value)# aca tiene que pintarme el nombre que puse en la vista user_api_view seria Valentino
    
    return value # para que me retorne el valor
 
  def validate_email(self,value): # aca tiene que pintarme el email que puse en la vista user_api_view seria valen@yahoo.com.ar
    
    print(value)
    
    return value
 

  def validate(self,data):
    print("validate general") # primero pinta esto y despues pinta el print de la vista
    return data
 
 # osea funciona asi primero pregunta si existe el nombre y el email con def validate_name y  def validate_email y por ultimo pasa al def validate