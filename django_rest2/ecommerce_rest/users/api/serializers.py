# creamos un serielizador para nuestro modelo usuario
# un sereilizador es cuando toma los datos de un modelo para convertirlos en json, para retornar un json

from rest_framework import serializers
from users.models import User

# ahora creo el serializazors, que me convierte a json

class UserSerializer(serializers.ModelSerializer): # va a ser un serielizadors basado en un modelo, por eso hereda de ModelSerializer
    
     class Meta:
       model =User
       fields = '__all__'   # si quiero campos especificos, hago como en el fields del formModels de django
       
    
    

