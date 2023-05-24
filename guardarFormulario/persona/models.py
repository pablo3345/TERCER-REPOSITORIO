from django.db import models
import datetime

# Create your models here.

pais_status = [("Argentina", "Argentina"), ("Colombia", "Colombia"), ("Peru", "Peru")] #es una tupla

class Personas(models.Model):
   
    fecha_inicio= models.DateTimeField(auto_now=False)
    fecha_final =models.DateTimeField(auto_now=False)
    
    #-----------------------------------------------------------------------------------------
    precio_noche = models.FloatField()
    precio_semana = models.FloatField(default=0)
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
        
        
        #--------------------check out 12-----------------------------
        
        '''if fechaConvertida2.hour ==12 and fechaConvertida2.minute ==00:
       
         if fechaConvertida.hour <12 and diferencia.days >00:
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
             
        else:
            #-----------------late check out ------------------------
            if fechaConvertida2.hour <=18: '''
                
        
     #--------------------------check out 10--------------------------
        if fechaConvertida2.hour ==10 and fechaConvertida2.minute ==00:
       
          if fechaConvertida.hour <10 and diferencia.days >00:
            
            diferenciaConvertida = diferencia.days
            diferenciaConvertida = diferenciaConvertida #+1
            print(diferenciaConvertida)
       
         
          elif fechaConvertida.hour >= 10 and fechaConvertida.minute>=1: #le agregue el = al 00
            
              diferenciaConvertida = diferencia.days
              diferenciaConvertida = diferenciaConvertida+1 #+2
              print(diferenciaConvertida, "(10) debo sumarle uno")
             
          elif fechaConvertida.hour ==10 and fechaConvertida.minute ==00:
              diferenciaConvertida = diferencia.days
              diferenciaConvertida = diferenciaConvertida #+1
         
              print("igual a 10 (10)", diferenciaConvertida)
              
          
             
        
          elif diferencia.days <1:
               diferenciaConvertida=1
               print("menos de un dia (10)", diferenciaConvertida)
               
          elif fechaConvertida.hour >= 10: #le agregue el = al 00
              diferenciaConvertida = diferencia.days
              diferenciaConvertida = diferenciaConvertida+1 #+2
              print(diferenciaConvertida, "(10) debo sumarle uno, para la hora 22")
              
              
      
             #---------------------late check out--------------------
             
        diferenciaGlobal = diferenciaConvertida
        diferenciaGlobal_late = diferenciaGlobal+0.5
        print(diferenciaGlobal, "diferencia global")
        print(diferenciaGlobal_late, "diferencia global late")
       
               
             
      
           
       
            
      
           
        '''if fechaConvertida2.hour >=10 and fechaConvertida2.hour <=17:
                print("entro al late chack out", diferenciaConvertida)
              
                if fechaConvertida.hour <10 and diferencia.days >00:
                   diferenciaConvertida = diferencia.days
                   diferenciaConvertida = diferenciaConvertida +0.5 #+1
                   print(diferenciaConvertida, "late")
                   
                elif fechaConvertida.hour >= 10 and fechaConvertida.minute>=1: #le agregue el = al 00
                    diferenciaConvertida = diferencia.days
                    diferenciaConvertida = diferenciaConvertida+1.5 #+2
                    print(diferenciaConvertida, "(10) debo sumarle uno (late)")'''
                
                 
             
        
    
        
               
            
      
            
             
#-------------------------check out 11----------------------------------------
        '''if fechaConvertida2.hour ==11 and fechaConvertida2.minute ==00:
       
         if fechaConvertida.hour <11 and diferencia.days >00:
           diferenciaConvertida = diferencia.days
           diferenciaConvertida = diferenciaConvertida #+1
           print(diferenciaConvertida)
       
         
         elif fechaConvertida.hour >= 11 and fechaConvertida.minute>00:
             diferenciaConvertida = diferencia.days
             diferenciaConvertida = diferenciaConvertida+1 #+2
             print(diferenciaConvertida, "(11) debo sumarle uno")
             
         elif fechaConvertida.hour ==11 and fechaConvertida.minute ==00:
             diferenciaConvertida = diferencia.days
             diferenciaConvertida = diferenciaConvertida #+1
         
             print("igual a 11 (11)", diferenciaConvertida)
             
         else:
             diferenciaConvertida=1
             print("menos de un dia (11)", diferenciaConvertida)'''
             

             
    
             
             
            
             
             
       
             
    
             
             
            
             
             
       