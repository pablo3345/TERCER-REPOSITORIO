from django.db import models

# Create your models here.

pais_status = [("Argentina", "Argentina"), ("Colombia", "Colombia"), ("Peru", "Peru")] #es una tupla

class Personas(models.Model):
   
    fecha_inicio= models.DateTimeField(auto_now=False)
    fecha_final =models.DateTimeField(auto_now=False)
    
    #-----------------------------------------------------------------------------------------
    precio_noche = models.FloatField()
    precio_semana = models.FloatField(null=True, blank=True)
    #----------------------------------fecha----------------------------------------------------------
    #fecha_inicio = models.DateTimeField(auto_now=False)
   # fecha_final = models.DateTimeField(auto_now=False)
    
    
    #--------------------------------------------------------------------------------------------------
    created = models.DateTimeField(auto_now_add=True)  # aca guardamos la fecha que se creo un servicio
    updated = models.DateTimeField(auto_now=True) # aca guardamos cuando se actualiza


    '''def __str__(self):
        return f'{self.nombre} {self.apellido}' '''

    class Meta:
         db_table = "personass"
         verbose_name = "Persona"
         verbose_name_plural = "Personas"
         ordering = ['id']  # significa que se va a ordenar por id




