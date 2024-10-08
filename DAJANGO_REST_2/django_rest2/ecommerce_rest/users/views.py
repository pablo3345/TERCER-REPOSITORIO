from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from users.api.serializers import UserTokenSerializer
from django.contrib.sessions.models import Session # esta clase es la que maneja las sesiones
from datetime import datetime
from rest_framework.views import APIView
# Create your views here.

from users.authentication_mixin import Authentication # traigo la clase Authentication que va a heredar en la clase de abajo UserToken
 
 
class UserToken(Authentication, APIView): # hago una vista para que me refresque el token
    
    # solo valida el token
   
    def get(self, request, *args, **kwargs):
      
        
       
        
        try:
            # aca me esta trayendo el usuario para este token, si no me trae este usuario entonces es un usuario que no ha iniciado sesion nunca
            user_token,_ = Token.objects.get_or_create(user=self.user)
            # no nos olvidemos que el metodo get_or_create devuelve dos cosas,  token,created 
            
            user = UserTokenSerializer(self.user)
            
            return Response({'token': user_token.key, 'user': user.data}) # solo me trae el token actual que esta en la bbdd, si se ha vencido no importa se volvera a hacer la peticion
        except:
        # que pasa si no me encuentra el token
          return Response({'error':'credenciales enviada incorrectas'}, status = status.HTTP_400_BAD_REQUEST) #HTTP_400_BAD_REQUEST significa mala peticion
        
    
    


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
           # si el usuario no esta activo puede ser que lo hayan desabilitado x alguna razon
                
              token,created = Token.objects.get_or_create(user=user) # lo que tiene el modelo Token es un campo llamado user, por eso aca filtro por usuario
              #esto quiere decir: traeme el token para este usuario, y si no existe me lo creas al token
              #get_or_created del ORM de django retorna dos cosas, la instancia y un booleano que dice si se a creado o no, si se ha creado es True
              user_serializer= UserTokenSerializer(user) # aca lo serializo y le mando el usuario
              if created: # si se ha creado el token
                  # aca pregunta si el token ha sido creado, si no ha sido creado xq tal vez ya existia, pasa directamente al mensaje de abajo (hola desde Response) y en Postman no me muestra el mensaje con todos los datos del usuario y el token 
               
                  
                  return Response({'token': token.key, 'user':user_serializer.data, 'mensaje': 'inicio de sesion exitoso'}, status=status.HTTP_201_CREATED) # el modelo Token tambien tiene un campo llamado key, la clave y tambien el usuario
              
              
              else:
                  
                  
                  
                  '''all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                  
                  if all_sessions.exists():
                      for session in all_sessions: #buscame la session que corresponda al usuario actual
                          session_data = session.get_decoded() # descodifico la sesion
                          if user.id  == int(session_data.get('_auth_user_id')): # el id del usuario a que corresponde la session es igual a la session que se esta iterando, entonces me borra la session
                              session.delete()
                              # se borra la sesion xq pudo haber pasado 2 cosas: alguin obtuvo mi usuario y contraseña, o se me ha vencido el token
                              # esto seria para cuando he iniciado session no quiero que vuelvan a iniciar session'''
                          
                   #------------------------------------------------------------------------------------------       
                          
                 
                      
                  token.delete() 
                  return Response({'error': 'ya se ha iniciado sesion con otro usuario'}, status=status.HTTP_409_CONFLICT)  
                  
                 
              
            else:
                return Response({'error': 'este usuario no puede iniciar sesión'}, status=status.HTTP_401_UNAUTHORIZED)
            
        else:
            return Response({'error': 'nombre de usuario o contraseña incorrecta'}, status=status.HTTP_400_BAD_REQUEST)
       # return Response({'mensaje': 'hola desde Response'}, status=status.HTTP_200_OK)
      
      
      
      # entonces el modelo por defecto de Token tiene un campo que se llama user el usuario, y otro que seria la key la clave
      
     
     
class Logaut(APIView): # tambien se puede crear una funcion con el decorador para que permita GET y POST a la vez
    
    #el Logaut se puede hacer por get o por post
    def get(self, request, *args, **kwargs):
        
     try: # esto es x si no me mandan la variable token, y si hay token hago todo lo de abajo
        token = request.GET.get('token') # si nos han mandado el token
        token = Token.objects.filter(key=token).first() #ya que el modelo Token tiene dos campos el usuario y la key, creo que la key es el token como tal
        
       
        
      
        
        if token:
            user=token.user # si hay token me traigo el usuario
             # como hago un logaut destruyo la sesion y el token
            all_sessions = Session.objects.filter(expire_date__gte = datetime.now())# esto se utiliza para filtrar las sesiones cuya fecha de expiracion es mayor o igual a la fecha actual, osea solo me traera sesiones cuya fecha no han expirado
                  
            if all_sessions.exists():
                for session in all_sessions: #buscame la session que corresponda al usuario actual
                    session_data = session.get_decoded() # descodifico la sesion
                    if user.id  == int(session_data.get('_auth_user_id')): # el id del usuario a que corresponde la session es igual a la session que se esta iterando, entonces me borra la session
                            session.delete()
                              # se borra la sesion xq pudo haber pasado 2 cosas: alguin obtuvo mi usuario y contraseña, o se me ha vencido el token
                              # esto seria para cuando he iniciado session no quiero que vuelvan a iniciar session
            
            
            token.delete()             
            session_message='Sesiones de usurio eliminado'
           
            token_message='Token eliminado'
        
            return Response({'token_message': token_message, 'session_message': session_message},status=status.HTTP_200_OK)
       
        return Response({'error':'no se ha encontrado el usuario con estas credenciales'},status=status.HTTP_400_BAD_REQUEST) # el else de arriba x si no ha encontrado el token
    
     except:
         return Response({'error':'no se ha encontrado token en la peticion'}, status=status.HTTP_409_CONFLICT)
        
       