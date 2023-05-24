from django.shortcuts import render, redirect
import datetime
from django import forms
from persona.models import Personas
from django.contrib import messages
from persona.forms import PersonaForm


#from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime

# Create your views here.



'''class DTForm():
  forms = PersonaForm()
  date_input = forms.DateField(widget=AdminDateWidget())
  time_input = forms.DateField(widget=AdminTimeWidget())
  date_time_input = forms.DateField(widget=AdminSplitDateTime())'''


def llenarPlanilla(request):
  
    form = PersonaForm()
    persona=Personas()
    fecha_inicios = request.POST.get("fecha_inicio")
   
  
    
    precio_semanas = request.POST.get("precio_semana")
    fecha_final = request.POST.get("fecha_final")
    #fecha_salidas = request.POST.get("fecha_final")
    nombre= request.POST.get("nonmbre")
    
   

  

    if request.method =='POST':
         fechaConvertida = datetime.datetime.strptime(fecha_inicios, '%Y-%m-%dT%H:%M') # strptime lo convierto a objeto datetime, el segundo parametro le dice como interpretar la fecha, cual es la hora, el dia, el mes etc
       # fechaFormateada = fecha.strftime('%d / %m / %Y')  #Para dar el formato que quiero
         fechaFormateada = fechaConvertida.strftime('%Y-%m-%dT%H:%M') 
         print("la fecha formateada es :", fechaFormateada)
        
         fechaConvertida2 = datetime.datetime.strptime(fecha_final, '%Y-%m-%dT%H:%M')
         fechaFormateada2 = fechaConvertida2.strftime('%Y-%m-%dT%H:%M') 
         
         precio_noches = request.POST.get("precio_noche")
         
          #......................convierto el dia en entero..................
       # VIDEO EN YOUTUBE 'MODULO DEATETIME: MANEJO DE FECHAS Y HORAS EN PYTHON'
         
         dia_entero =  int(fechaConvertida.strftime('%d')) #con esto transformo el dia a entero
         
          #.........................comparar fechas (todas se comparan con datetime)..............
         fechaConvertida = datetime.datetime.strptime(fecha_inicios, '%Y-%m-%dT%H:%M')
         fechaConvertida2 = datetime.datetime.strptime(fecha_final, '%Y-%m-%dT%H:%M')
         
         diferencia = fechaConvertida2-fechaConvertida
         
         #print("la diferencia de dias es ", diferencia)
         
         
         
        
        
          
         #...........poner un delta de fecha para que me calcule a partir de 5 dias por ejemplo. (tambien con datetime)..........
         
         dia_delta = datetime.timedelta(days=5)#timedelta es una instacia de datetime
        # fechaInicial = datetime.date.today() #fecha de hoy creo (con esta fecha me funcionaba bien)
       
         
         
         #-------------------fecha en formato isoFormat (puede ser util para otra cosa)-----------
         
         fecha = datetime.datetime.now().isoformat()
       
        
         #...................................probando codigo para el hotel..............................
         
         
        
         #print(fechaConvertida.weekday())
         
       
        
         """ if fechaConvertida.hour <12:
           diferenciaConvertida = diferencia.days
           diferenciaConvertida = diferenciaConvertida #+1
           print(diferenciaConvertida)
         elif fechaConvertida.hour >= 12 and fechaConvertida.minute>00:
             diferenciaConvertida = diferencia.days
             diferenciaConvertida = diferenciaConvertida+1 #+2
             print(diferenciaConvertida, "debo sumarle dos")
             
         elif fechaConvertida.hour ==12 and fechaConvertida.minute ==00:
             diferenciaConvertida = diferencia.days
             diferenciaConvertida = diferenciaConvertida #+1
         
             print("igual a 12", diferenciaConvertida)
              """
        
        
         
           
           
           
           
           
         
         
        
       
      
       
         
           #dia_delta = datetime.timedelta(hauers=24)
       
           #print("las noches a cobrar son", diferenciaConvertida)
          
         
          
           
            
         
  
 
  
       
      
        
        
         if form.is_valid:
              
              persona.precio_noche=precio_noches
              persona.precio_semana=precio_semanas
              persona.fecha_inicio=fechaFormateada
              persona.fecha_final=fechaFormateada2
              persona.nonmbre=nombre
             
              try:
              
                     #persona.save()
                     persona.calcularFechas(fecha_inicios, fecha_final)
                    
                     messages.success(request, "la Persona se guardo correctamente")
               
               
              except:
                    
                     messages.error(request, "la Persona no se guardo correctamente")
              
              return redirect('LLenarPlanilla')
        
        
           
    else:
        form = PersonaForm() # si no es un post le decimos que nos vuelva a renderizar el formulario


    return render(request,  'persona/planilla.html', {'form': form}) 



  

         
         
         
  
 
  
  
  
 