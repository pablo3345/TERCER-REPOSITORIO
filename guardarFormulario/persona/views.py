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
    
  
    precio_noches = request.POST.get("precio_noche")
    precio_semanas = request.POST.get("precio_semana")
    fecha_inicios = request.POST.get("fecha_inicio")
    #fecha_salidas = request.POST.get("fecha_final")
    
   

  

    if request.method =='POST':
         fechaConvertida = datetime.datetime.strptime(fecha_inicios, '%Y-%m-%dT%H:%M') # strptime lo convierto a objeto datetime, el segundo parametro le dice como interpretar la fecha, cual es la hora, el dia, el mes etc
       # fechaFormateada = fecha.strftime('%d / %m / %Y')  #Para dar formato a la fecha la que quiero
         fechaFormateada = fechaConvertida.strftime('%Y-%m-%dT%H:%M') 
         print("la fecha formateada es :", fechaFormateada)
        
         fechaConvertida2 = datetime.datetime.strptime(fecha_inicios, '%Y-%m-%dT%H:%M')
         fechaFormateada2 = fechaConvertida2.strftime('%Y-%m-%dT%H:%M') 
         
        
         if form.is_valid:
              
              persona.precio_noche=precio_noches
              persona.precio_semana=precio_semanas
              persona.fecha_inicio=fechaFormateada
              persona.fecha_final=fechaFormateada2
              
              try:
              
               persona.save()
               messages.success(request, "la Persona se guardo correctamente")
               
               
              except:
                    
               messages.error(request, "la Persona no se guardo correctamente")
              
              return redirect('LLenarPlanilla')
        
        
              
              
              
      
       
      
        
        
        
        
        
      
       
       # form =PersonaForm(request.POST)
       # if form.is_valid(): #vamos a preguntar si los datos que se ingresaron son validos
       
     
         
             #
              
     
           #messages.add_message(request=request, level= messages.SUCCESS, message= "la Persona se guardo correctamente")
      



    else:
        form = PersonaForm() # si no es un post le decimos que nos vuelva a renderizar el formulario


    return render(request,  'persona/planilla.html', {'form': form}) 



  #   nombres = request.POST.get('nombre')#  con esto parece que obtengo el dato del input text del html, xq al input le puse el nombre



    #return render(request, "persona/planilla.html")



