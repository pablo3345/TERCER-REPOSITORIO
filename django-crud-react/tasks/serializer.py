from rest_framework import serializers
from .models import Task # el punto significa que esta en la misma carpeta tasks

class TaskSerializer(serializers.ModelSerializer):

  class Meta():
      
      model=Task
      
      filds= ('id', 'title', 'description', 'done') # esto es una tupla, recordar poner el id aunque en el modelo no lo pusimos
      #fields= '__all__' tambien puedo ponerlo asi
      