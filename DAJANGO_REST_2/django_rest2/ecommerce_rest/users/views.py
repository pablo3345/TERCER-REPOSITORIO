from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from users.api.serializers import UserTokenSerializer
# Create your views here.

class Login(ObtainAuthToken): # ObtainAuthToken lo que hace es una vista normal que creo que dijo que hereda de ApiView
    # ObtainAuthToken ya tiene dos campos definidos el username y el password
    # ObtainAuthToken no permite el metodo get, por eso para probar el login no podemos usar la interfaz de django rest framework
    # el token se asocia a un usuario
    def post(self, request, *args, **kwargs): # esto seria para el username y password del login
        
       # print(request.user)
        login_serializer= self.serializer_class(data = request.data, context={'request':request}) 
        
        if login_serializer.is_valid(): # si ha pasado la validacion 
            
            print("paso la validacion")
           # print(login_serializer.validated_data['user']) # validate_data xq en el serializador por defecto de authtoken la funcion validate nos esta devolviendo un user
            user = login_serializer.validated_data['user'] # aca obtengo mi usuario, validate_data xq en el serializador por defecto de authtoken esta en la funcion validate
            if user.is_active: #aca pregunto si mi usuario esta activo, no vale la pena seguir si mi usuario no esta activo x eso pregunto esto
          
                
              token,created = Token.objects.get_or_create(user=user) # lo que tiene el modelo Token es un campo llamado user, por eso aca filtro por usuario
              #esto quiere decir: traeme el token para este usuario, y si no existe me lo creas al token
              #get_or_created del ORM de django retorna dos cosas, la instancia y un booleano que dice si se a creado o no, si se ha creado es True
              user_serializer= UserTokenSerializer(user) # aca lo serializo y le mando el usuario
              if created: # si se ha creado el token
                  # aca pregunta si el token ha sido creado, si no ha sido creado xq tal vez ya existia, pasa directamente al mensaje de abajo (hola desde Response) y en Postman no me muestra el mensaje con todos los datos del usuario y el token 
               
                  
                  return Response({'token': token.key, 'user':user_serializer.data, 'mensaje': 'inicio de sesion exitoso'}, status=status.HTTP_201_CREATED) # el modelo Token tambien tiene un campo llamado key, la clave y tambien el usuario
            else:
                return Response({'error': 'este usuario no puede iniciar sesión'}, status=status.HTTP_401_UNAUTHORIZED)
            
        else:
            return Response({'error': 'nombre de usuario o contraseña incorrecta'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje': 'hola desde Response'}, status=status.HTTP_200_OK)
      
      
      
      # entonces el modelo por defecto de Token tiene un campo que se llama user el usuario, y otro que seria la key la clave
      
     