from rest_framework.views import APIView # seria como una vista en django
from users.models import User
from users.api.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view #un decorador para las vistas basadas en funcion y no de clases

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
        
        users = User.objects.all()
        userSerializer = UserSerializer(users, many=True)# con meny=True, le digo que no me traiga un users, sino todo el listado de users, aca me lo convierte en json
        
        return Response(userSerializer.data) # pongo userSerializer xq esa variable me contiene el json y agregarle .data para que me retorne el json
    
    
   elif request.method=='POST': # sino lo envia por get puede enviarlo por post y desde la pagina puedo crear un superusuario pasandole el json 
      user_serializer = UserSerializer(data = request.data) # creo la variable y con el serializador creo un modelo en json
      if user_serializer.is_valid(): # aca antes en django comun funcionado un Form a igual para los errores
          user_serializer.save()
          return Response(user_serializer.data) # cuando el serializador guarda la informacion se guarda en data y con return retorna dicha informacion
      
      return Response(user_serializer.errors) # si no es valido, va a retornar los errores y ubicar esos errores
          
        
        

@api_view(['GET', 'PUT', 'DELETE']) # para obtener un usuario con el id, para actualizar en Rest se usa el metodo PUT
def user_detail_view(request, pk=None):
    if request.method=='GET':
       user = User.objects.filter(id =pk).first() # first seria el primer elemento
       # aca podria hacerlo diferente ej: poner un mensaje si el pk en None, o podria hacerlo como en django comun
       user_serializer = UserSerializer(user) # aca le paso el usuario y no pongo many=True xq quiero obtener un solo objeto y no la lista completa de usuarios
       return Response(user_serializer.data)
   
    elif request.method=='PUT': # para actualizar un usuario en rest se usa el metodo PUT
         user = User.objects.filter(id =pk).first() # first seria el primer elemento
         user_serializer=UserSerializer(user, data=request.data) # sea PUT o POST con request.data llega la informacion al serielizador
         # a diferencia del POST aca en el PUT le envio el user que es la instacia que se va actualizar y luego el data=request.data
         if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        
         return Response(user_serializer.errors) # aca a esto lo pone como el elif del if de is_valid, pero sin el elif
     
    elif request.method == 'DELETE':
          user = User.objects.filter(id =pk).first() # first seria el primer elemento
          user.delete()
          return Response('Eliminado!')