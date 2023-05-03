from django.shortcuts import render, redirect
from django import forms
from persona.models import Personas
from django.contrib import messages
from persona.forms import PersonaForm
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime

# Create your views here.



'''class DTForm():
  forms = PersonaForm()
  date_input = forms.DateField(widget=AdminDateWidget())
  time_input = forms.DateField(widget=AdminTimeWidget())
  date_time_input = forms.DateField(widget=AdminSplitDateTime())'''


def llenarPlanilla(request):
  

    if request.method =='POST':

        form =PersonaForm(request.POST)
        if form.is_valid(): #vamos a preguntar si los datos que se ingresaron son validos
           form.save()
           messages.success(request, "la Persona se guardo correctamente")

           #messages.add_message(request=request, level= messages.SUCCESS, message= "la Persona se guardo correctamente")
           return redirect('LLenarPlanilla')








    else:


        form = PersonaForm() # si no es un post le decimos que nos vuelva a renderizar el formulario


    return render(request,  'persona/planilla.html', {'form': form})



  #   nombres = request.POST.get('nombre')#  con esto parece que obtengo el dato del input text del html, xq al input le puse el nombre



    return render(request, "persona/planilla.html")



