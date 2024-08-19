from django.db import models

# Create your models here.

class Task(models.Model):
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True) # como la descripcion puede ser un poco mas extensa, como un  texto, le pongo charfield,
    # y blanck true es porque si quiero no le pongo nada
    done= models.BooleanField(default=False) # si una tarea fue realizada, apenas se crea esta en False
    
    def __str__(self):
        
        return self.title
    
    
