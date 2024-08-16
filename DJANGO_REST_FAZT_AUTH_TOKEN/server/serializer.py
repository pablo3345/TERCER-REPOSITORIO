from rest_framework import serializers
from django.contrib.auth.models import User # django ya nos da un modelo usuario x defecto sin crear el modelo

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = User
        fields= ['id', 'username', 'email', 'password']

