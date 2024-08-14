from rest_framework import serializers
from projects.models import Projects

class ProyectsSerializers(serializers.ModelSerializer):
    class Meta:
        
        model=Projects
        fields=['id', 'title', 'description', 'technology', 'created_at'] #en el modelo no puse id, pero el campo id se crea automaticamente
        read_only_fields= ('created_at', ) # campo de solo lectura, le digo esto xq quiero que no modifiquen, editen o eliminen la fecha de creacion
        
        
        