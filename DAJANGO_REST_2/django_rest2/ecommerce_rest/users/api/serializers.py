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
  
  def validate_name(self,value): # validaciones
    
    #print(value)# aca tiene que pintarme el nombre que puse en la vista si estaria el print user_api_view seria Valentino
    # esto es una validacion personalizada, cuando es basado en un modelo no ahorramos estas validaciones
    if 'ghdrhfdhdrh' in value: # fijarme que Vele, Valen, Valentino me lo reconoce como true tambien
      raise serializers.ValidationError('no puede existir un usuario con ese nombre')
   # print(value) 
   
    print(self.context) # accedo al context que en la vista lo puse para obtener todo el diccionario y no solo al name
    
    return value # para que me retorne el valor
  # validacion personalizada, cuando es basado en un modelo no ahorramos estas validaciones
  def validate_email(self,value): # aca tiene que pintarme el email que puse en la vista user_api_view seria valen@yahoo.com.ar
    if value =="":
       raise serializers.ValidationError('tiene que indicar un correo')
   # print(value)
   
    '''if self.context['name'] in value: # aca estando solo en el email puedo acceder al name xq en la vista le agregue el contexto (context), para obtener todo el diccionario
       raise serializers.ValidationError('el nombre no puede pertenecer al correo')'''
     # tambien puedo llamar a la funcion de arriba del name para validar correctamente ej if self.validate_name(self.context['name']) in value: 
    return value
 

  def validate(self,data): # como aca ya no tengo los campos independientes sino el conjunto de campos con data, pero conviene usarlo para otro tipos de error xq asi no me indica el error especifico del name o email
   # if data['name'] in data['email']:
       # raise serializers.ValidationError('el nombre no puede pertenecer al correo')
   # print("validate general") # primero pinta esto y despues pinta el print de la vista
    return data
 
 # osea funciona asi primero pregunta si existe el nombre y el email con def validate_name y  def validate_email y por ultimo pasa al def validate
 
  def create(self, validated_data): # create es cuando hago un post o sea cuando guardo un usuario, validated_data es simplemente la informacion validada que recibio el serializador
   return User.objects.create(**validated_data) # es un diccionario entonces con los dos ** le digo a python que tenga en cuenta los valores y no las claves, y pongo User xq debe tener un modelo para guardar
  # print(validated_data)
  
  
  # aparentemente haciendo un print parece que primero ejecuta lo que hay dentro de la funcion del serializer y luego lo de la vista
  
  def update(self, instance,validated_data ):# es para el metodo actualizar del PUT de la vista, esta funcion updated recibe instance(pero de la vista no la envie a la instance) y  validated_data para validar los datos
   instance.name = validated_data.get('name', instance.name)
   instance.email = validated_data.get('email', instance.email)# asi seria para actualizarlo a mano
   instance.save() # desde la interfaz de ayuda del PUT le envio el diccionario con los nuevos valores, este save() pertenece a una clase osea al modelo, es propia del modelo
    # osea funciona asi...el save() de la vista llama al metodo del serializador create() o updated(), y el save() del serializador created() o updated() llama al modelo, clase y lo guarda... (aclaro este save() es de guardar NO DE LA FUNCION SAVE() DE ABAJO)
   
   return instance # y retorno la instancia
 
 
 
 
 
  #def save(self): # puedo usar este metodo x ejemplo para enviar un correo, por ej sirve para un formulario de contacto, pero sin guardar registros
    # no nos olvidemos que como en la vista esta el is_valid() primero pasa por las todas las validaciones de arriba
    
   # print(self)
    #send_mail()
 
#termine el video 12