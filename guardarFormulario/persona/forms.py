from django import forms
from persona.models import Personas
from django.contrib.admin.widgets import AdminDateWidget

'''class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local' '''


class DateInput(forms.DateInput):
    input_type = 'date' 

class PersonaForm(forms.ModelForm):

    class Meta:
        model= Personas
        
   
    
        
        
        fields = [  #aca en esta tupla ponemos los campos del modelo que queremos utilizar

            'nombre',
            'apellido',
            'mail',
            'edad',
            'telefono',
            'sexo',
            'direccion',
            'ciudad',
            'pais',
            'codigo_postal',
            'mensaje',
            'fecha_inicio2',
            'fecha_final2',
          


        ]

        labels ={       # aca en este diccionario pongo las etiqetas que quiero que tengan los textxField en el html
        
            'nombre':'Nombre*',
            'apellido':'Apellido*',
            'mail': 'Mail*',
            'edad': 'Edad*',
            'telefono':'Telefono*',
            'sexo':'Sexo',
            'direccion':'Direccion*',
            'ciudad':'Ciudad*',
            'pais':'Pais*',
            'codigo_postal':'Codigo Postal*',
            'mensaje':'mensaje',
            'fecha_inicio2': 'fecha inicio*',
            'fecha_final2': 'fecha final*',
         


        }

        widgets ={ # lo que se va a ver en el formulario del html
            'nombre': forms.TextInput(),
            'apellido':forms.TextInput(),
            'mail':forms.EmailInput(),
            'edad':forms.TextInput(),
            'telefono':forms.TextInput(),
            'sexo':forms.RadioSelect(),
            'direccion': forms.TextInput(),
            'ciudad': forms.TextInput(),
            'pais':forms.Select(),
            'codigo_postal': forms.TextInput(),
            'mensaje': forms.Textarea(),
            'fecha_inicio2': DateInput(),
            'fecha_final2': DateInput()
                
         
          
            
            
            #attrs={'class':'form-row'} poner en () ejemplo TextInput() seria la clase de bootdtrap
            #attrs={'placeholder':'Phone Number'} poner esto en el text input en gris pero que se puede escribir arriba de la palabra


        }







