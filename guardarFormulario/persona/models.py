from django.db import models

# Create your models here.

pais_status = [("Argentina", "Argentina"), ("Colombia", "Colombia"), ("Peru", "Peru")] #es una tupla

class Personas(models.Model):
    nombre =models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    mail = models.EmailField()
    edad = models.IntegerField()
    telefono = models.CharField(max_length=40)
    sexo = models.CharField(max_length=6, choices=(('M', 'masculino'), ('F', 'femenino'), ('OTRO', 'otro')), default=1)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    pais= models.CharField(max_length=15,  null= False, blank=False, choices=pais_status, default= 1)#con default = 1 me aparece solo los valores que escribi arriba y no esa line discontinua que molesta
    codigo_postal = models.IntegerField()
    mensaje= models.TextField()
    fecha_inicio2= models.DateField()
    fecha_final2 =models.DateField()
    #----------------------------------fecha----------------------------------------------------------
    #fecha_inicio = models.DateTimeField(auto_now=False)
   # fecha_final = models.DateTimeField(auto_now=False)
    
    
    #--------------------------------------------------------------------------------------------------
    created = models.DateTimeField(auto_now_add=True)  # aca guardamos la fecha que se creo un servicio
    updated = models.DateTimeField(auto_now=True) # aca guardamos cuando se actualiza


    '''def __str__(self):
        return f'{self.nombre} {self.apellido}' '''

    class Meta:
         db_table = "personas"
         verbose_name = "Persona"
         verbose_name_plural = "Personas"
         ordering = ['id']  # significa que se va a ordenar por id




