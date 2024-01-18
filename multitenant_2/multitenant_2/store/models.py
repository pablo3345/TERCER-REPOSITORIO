from django.db import models

# Create your models here.

#los modelos que esten aqui van a permanacer a un solo cliente

# no pongo clave foranea xq es solo un modelo de prueba

class Product(models.Model):
    
    name = models.CharField(max_length=50)
    description= models.TextField()
    stock= models.IntegerField()
    
    def __str__(self):
        return self.name
    
    
class Category(models.Model):
      name = models.CharField(max_length=50)
    
      description= models.TextField()
      
      def __str__(self):
        return self.name
    
