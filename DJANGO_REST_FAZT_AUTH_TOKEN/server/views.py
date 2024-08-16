from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import UserSerializer # como estoy en la misma carpeta pongo el punto .
from django.contrib.auth.models import User # django ya nos da un modelo usuario x defecto sin crear el modelo
from rest_framework.authtoken.models import Token
from rest_framework import status

@api_view(['POST'])
def login(request):
    
    
    return Response({})
    
    
    

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
   





@api_view(['POST'])
def perfil(request):
    
    
     return Response({})
 
 
 