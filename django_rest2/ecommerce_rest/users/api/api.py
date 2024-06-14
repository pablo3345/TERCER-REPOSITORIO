from rest_framework.views import APIView # seria como una vista en django
from users.models import User
from users.api.serializers import UserSerializer
from rest_framework.response import Response

class UserApiView(APIView): # es como una vista en django
    
    def get(self, request): # este metodo get va a recibir la peticion que me envie el front End
        
        users = User.objects.all()
        userSerializer = UserSerializer(users, many=True)# con meny=True, le digo que no me traiga un users, sino todo el listado de users, aca me lo convierte en json
        
        return Response(userSerializer.data) # pongo userSerializer xq esa variable me contiene el json y agregarle .data para que me retorne el json
    
        
    

