from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import UserSerializer # como estoy en la misma carpeta pongo el punto .
from django.contrib.auth.models import User # django ya nos da un modelo usuario x defecto sin crear el modelo
from rest_framework.authtoken.models import Token
from rest_framework import status 
from django.shortcuts import get_object_or_404 # esto significa que me vas a buscar un objeto dentro de la bbdd, y si no lo encuentra me vas a retornar un error 404

#estas importaciones es para la vista perfil
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated # para saber quie esta autenticado, o que ruta puede visitar si un usuario esta autenticado
from rest_framework.authentication import TokenAuthentication

@api_view(['POST'])
def login(request): # primero vamos a controlar si el username y la contraseña existe, tambien se puede controlar por email si deseo
    
    user = get_object_or_404(User, username= request.data['username']) # aca obtengo el usuario, con request.data
    if not user.check_password(request.data['password']): #vamos a validar su contraseña, check_password sirve para comparar un string con la contraseña ya encriptada, entonces solo tengo que pasarle el password
    # esto seria que el usuario me esta retornando un False x su contraseña erronea, entonces pongo un error invalid password, si esto no se da, osea que la contraseña enviada x el usuario es valida True pasa abajo
      return Response({'error':'password invalida'}, status=status.HTTP_400_BAD_REQUEST)
  
    #---ahora creamos el token----
    
    #esto seria como el else del if de arriba
    token, created = Token.objects.get_or_create(user=user) # created es un booleano que me dice si el token se creo o no
    serializer = UserSerializer(instance=user) # esto me va a dar un dato serializado en objeto json, osea un diccionario de la instancia del usuario
    
   
    
    return Response({'token': token.key, 'usuario': serializer.data}, status=status.HTTP_200_OK)
    
    
    

@api_view(['POST'])
def register(request):
    
    serializer = UserSerializer(data= request.data)
    
    if serializer.is_valid(): # si es valido significa que el frontend me esta enviando los datos correctos
        serializer.save() # como este serializer es correcto y lo tengo guardado, ahora voy a crear un nuevo modelo en la bbdd seria User
        
        user = User.objects.get(username = serializer.data['username']) # aca obtengo el username que que me ha enviado el frontend, que lo busque en el serializer de arriba, y me da un usuario nuevo
        user.set_password(serializer.data['password']) # aca la contraseña ya esta encriptada, voy a establecer una contraseña que esta viniendo del frontend
        user.save() # y finalmente guardamos este usuario en la bbdd
        #aca podemos agragar mas campos
        
        
        #una vez que el usuario esta guardado en la bbdd, ahora generamos un token
   
        token = Token.objects.create(user=user) # aca me da un toquen para el usario
        
       
        
        return Response({'Token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED) #·me vas a retornar el token como tal
    
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # es como el else de si los datos que me ha enviado el frontend no son validos
   





@api_view(['POST']) # aca puede ser GET o POST
@authentication_classes([TokenAuthentication]) # esta propiedad significa que me tiene que enviar un header con el token
@permission_classes([IsAuthenticated]) # esto significa que esta vista o ruta esta protegida osea tiene que estar autenticada
def perfil(request):
    
     print(request.user) # con esto ya veo el usuario
    
     #serializer = UserSerializer(instance=request.user) # aca serializo el usuario y obtengo una instancia del usuario y luego lo puedo poner en el return Response
     
     return Response("tu haz hecho login con: {}".format(request.user.username), status=status.HTTP_200_OK)
 
 
 
'''@api_view(['GET']) # esto lo invente yo no estaba en el tutorial
def logaut(request):
    user = get_object_or_404(User, username= request.data['username'])
    token = Token.objects.filter(user = user).first()
    
    print("el token es:", token)
    
    
    token.delete()
    
    # aca tambien se puede poner eliminar la sesion
    
    
    return Response({})'''