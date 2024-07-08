from rest_framework.views import APIView # seria como una vista en django
from users.models import User
from users.api.serializers import UserSerializer, TestUserSerializador, UserListSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view #un decorador para las vistas basadas en funcion y no de clases
from rest_framework import status
#una vista basada en clase

'''class UserApiView(APIView): # es como una vista en django
    
    def get(self, request): # este metodo get va a recibir la peticion que me envie el front End
        
        users = User.objects.all()
        userSerializer = UserSerializer(users, many=True)# con meny=True, le digo que no me traiga un users, sino todo el listado de users, aca me lo convierte en json
        
        return Response(userSerializer.data) # pongo userSerializer xq esa variable me contiene el json y agregarle .data para que me retorne el json'''
    
        
    
#una vista basada en funcion
'''@api_view(['GET', 'POST']) # va GET o POST (puedo usar uno o ambos) xq es el metodo http que va a permitir
def user_api_view(request): # es una vista basada en funcion x eso va request
    
   if request.method == 'GET':
        
        users = User.objects.all()
        userSerializer = UserSerializer(users, many=True)# con meny=True, le digo que no me traiga un users, sino todo el listado de users, aca me lo convierte en json
        
        return Response(userSerializer.data) # pongo userSerializer xq esa variable me contiene el json y agregarle .data para que me retorne el json
    
    
   elif request.method=='POST': # sino lo envia por get puede enviarlo por post y desde la pagina puedo crear un superusuario pasandole el json 
       print(request.data) # en request.data almacena los datos del POST '''
       
    
#una vista basada en funcion
@api_view(['GET', 'POST']) # va GET o POST (puedo usar uno o ambos) xq es el metodo http que va a permitir
def user_api_view(request): # es una vista basada en funcion x eso va request
    
   if request.method == 'GET':
        
        users = User.objects.all().values('id', 'username', 'email', 'password')# con values obtengo solo esos campos y se lo envio al metodo del serializador  def to_representation(self, instance):
       # userSerializer = UserSerializer(users, many=True)# con meny=True, le digo que no me traiga un users, sino todo el listado de users, aca me lo convierte en json
        userSerializer = UserListSerializer(users, many=True)
        #----------------------------------------------------------------------------------------------
        # aqui creo el diccionario para enviarle al serializador, class TestUserSerializador(serializers.Serializer):
        
        
        #---esto lo use para el seializador  def create(self, validated_data):
        '''test_data={'name': 'Carlos', 
                   'email': 'calo@yahoo.com.ar'}
        
        
        test_user= TestUserSerializador(data=test_data, context=test_data) # con context=test_data le envio todo el diccionario
        if test_user.is_valid():
           user_instance = test_user.save()
           print("paso la validacion el test_user...")
           
        else:
           print(test_user.errors)'''
       #------------------------------------------------------------------------- 
        
        
        #-------------------------------------------------------------------------------------------------
        return Response(userSerializer.data, status= status.HTTP_200_OK) # pongo userSerializer xq esa variable me contiene el json y agregarle .data para que me retorne el json
     # el status para obtener un usuario con GET seria 200 correcto ok
    
   elif request.method=='POST': # sino lo envia por get puede enviarlo por post y desde la pagina puedo crear un superusuario pasandole el json 
      user_serializer = UserSerializer(data = request.data) # creo la variable y con el serializador creo un modelo en json
      if user_serializer.is_valid(): # aca antes en django comun funcionado un Form a igual para los errores
          user_serializer.save()
          return Response({'message': 'El usuario se creo correctamente'}, status= status.HTTP_201_CREATED) # cuando el serializador guarda la informacion se guarda en data y con return retorna dicha informacion, no quiero que me muestre la instancia(usuario) x eso pongo solo el mensaje
       # el status es correspondiente a creado un usuario, aparece en la documentacion de rest en API GUIDE como status code
      
      return Response(user_serializer.errors, status= status.HTTP_400_BAD_REQUEST) # si no es valido, va a retornar los errores y ubicar esos errores
          
       
        

@api_view(['GET', 'PUT', 'DELETE']) # para obtener un usuario con el id, para actualizar en Rest se usa el metodo PUT
def user_detail_view(request, pk=None):
   
   user = User.objects.filter(id =pk).first() # first seria el primer elemento, aca traigo el usuario segun el id, seria una querySet
   
   if user: # va a devolver un booleano, si hay usuario pasa a los metodos de abajo, seria la validacion
   
    if request.method=='GET':
     
       # aca podria hacerlo diferente ej: poner un mensaje si el pk en None, o podria hacerlo como en django comun
       user_serializer = UserSerializer(user) # aca le paso el usuario y no pongo many=True xq quiero obtener un solo objeto y no la lista completa de usuarios
       return Response(user_serializer.data, status= status.HTTP_200_OK)
   
    elif request.method=='PUT': # para actualizar un usuario en rest se usa el metodo PUT
        
         user_serializer=UserSerializer(user, data=request.data) # sea PUT o POST con request.data llega la informacion al serielizador
          # user_serializer=TestUserSerializador(user, data=request.data) 
       #  user_serializer=TestUserSerializador(user, data=request.data) # llamo al serializador TestUserSerializador pero le envio la instancia del modelo user, y con data=request.data obtengo los datos
         # a diferencia del POST aca en el PUT le envio el user que es la instacia que se va actualizar y luego el data=request.data
         if user_serializer.is_valid():
            user_serializer.save() # cuando pongo .save() llamo a la funcion del serializador  def create(self, validated_data), o a la funcion del updated
            print(user_serializer.data) # con esto muestro los datos
            return Response(user_serializer.data, status= status.HTTP_200_OK)
         # como en la documentacion no aparecia ningun status para actualizado con 200 ok esta bien
        
         return Response(user_serializer.errors, status= status.HTTP_400_BAD_REQUEST) # aca a esto lo pone como el elif del if de is_valid, pero sin el elif
     
    elif request.method == 'DELETE':
        
          user.delete()
          return Response({'message': 'Usuario eliminado correctamente...'}, status= status.HTTP_200_OK)# un diccionario para los errores el fron end va interpretar la variable message
       
       
   return Response({'message': 'no se ha encontrado el usuario con esos datos'}, status= status.HTTP_400_BAD_REQUEST)# si no hay usuario me retornas este mensaje, aca seria como el else del if de arriba, y error 400 xq si no encontro el usario debe haber un error
   
   
   # SI A ESTAS FUNCIONES LA PASO A (viewsets.ModelViewSet): O A (ViewSet.GenericViewSet) ENTONCES ME APARECE EN LA INTERFAZ SWAGGER, FIJARME QUE OTRAS NO