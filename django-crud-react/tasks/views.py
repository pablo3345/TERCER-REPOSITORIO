

# Create your views here.

from rest_framework import viewsets
from .serializer import TaskSerializer
from .models import Task



class TaskView(viewsets.ModelViewSet):
    
    serializer_class= TaskSerializer # con esto le digo el modelo serializado que quiero trabajar
    
    queryset= Task.objects.all() # para que me traiga todos los campos del modelo


