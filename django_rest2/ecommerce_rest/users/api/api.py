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
@api_view(['GET', 'POST']) # va GET o POST (puedo usar uno o ambos) xq es el metodo http que va a permitir
def user_api_view(request): # es una vista basada en funcion x eso va request
    
   if request.method == 'GET':
        
        users = User.objects.all()
        userSerializer = UserSerializer(users, many=True)# con meny=True, le digo que no me traiga un users, sino todo el listado de users, aca me lo convierte en json
        
        return Response(userSerializer.data) # pongo userSerializer xq esa variable me contiene el json y agregarle .data para que me retorne el json'''
    
    
   elif request.method=='POST': # sino lo envia por get puede enviarlo por post y desde la pagina puedo crear un superusuario pasandole el json
       print(request.data) # en request.data almacena los datos del POST
       
       
    
        

