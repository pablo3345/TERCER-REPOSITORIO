from django.db import models
import datetime

# Create your models here.

pais_status = [("Argentina", "Argentina"), ("Colombia", "Colombia"), ("Peru", "Peru")] #es una tupla

class Personas(models.Model):
   
    fecha_inicio= models.DateTimeField(auto_now=False)
    fecha_final =models.DateTimeField(auto_now=False)
    
    #-----------------------------------------------------------------------------------------
    precio_noche = models.FloatField()
    precio_semana = models.FloatField(null= True)
    #----------------------------------fecha----------------------------------------------------------
    #fecha_inicio = models.DateTimeField(auto_now=False)
   # fecha_final = models.DateTimeField(auto_now=False)
   
    nonmbre = models.CharField(max_length=10, unique=True)
    
    
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
         
         
    def calcularFechas(request, fecha_inicios, fecha_final):
       
        
        fechaConvertida = datetime.datetime.strptime(fecha_inicios, '%Y-%m-%dT%H:%M') # strptime lo convierto a objeto datetime, el segundo parametro le dice como interpretar la fecha, cual es la hora, el dia, el mes etc
        fechaConvertida2 = datetime.datetime.strptime(fecha_final, '%Y-%m-%dT%H:%M')
         
        diferencia = fechaConvertida2-fechaConvertida
       
        if fechaConvertida.hour <12 and diferencia.days >0:
           diferenciaConvertida = diferencia.days
           diferenciaConvertida = diferenciaConvertida #+1
           print(diferenciaConvertida)
       
         
        elif fechaConvertida.hour >= 12 and fechaConvertida.minute>00:
             diferenciaConvertida = diferencia.days
             diferenciaConvertida = diferenciaConvertida+1 #+2
             print(diferenciaConvertida, "debo sumarle uno")
             
        elif fechaConvertida.hour ==12 and fechaConvertida.minute ==00:
             diferenciaConvertida = diferencia.days
             diferenciaConvertida = diferenciaConvertida #+1
         
             print("igual a 12", diferenciaConvertida)
             
        else:
             diferenciaConvertida=1
             print("menos de un dia", diferenciaConvertida)
             
       
             
        
       
       
          
             
      
             
       



