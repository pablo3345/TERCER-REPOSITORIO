from .models import Projects # importo el modelo
from rest_framework import viewsets, permissions
from projects.serializers import ProyectsSerializers

from rest_framework.response import Response
from rest_framework import status

class ProjectViewsets(viewsets.ModelViewSet):
    
    queryset=Projects.objects.all() # en esta consulta, consulto todos los datos de una tabla
    permission_classes =[permissions.AllowAny] # esto significa los permisos, de quien tiene permitido hacer operaciones con las consultas,
    # osea los clientes o las aplicaciones clientes va a poder solicitar datos a mi servidor
    # puedo cambiar AllowAny x isAuthenticated por ejemplo tiene permitido a quien este autenticado
    
    serializer_class =ProyectsSerializers # aca llamamos a nuestro serializer
    
    # segun dijo Fazt con solo esto ya tengo el CRUD completo para desplegarlo en el frontend en un movil etc
    
  
     
  
        
        
       
       
     