from django import forms
from persona.models import Personas


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local' 
    
    
    

    



   

class PersonaForm(forms.ModelForm):
  
  
       

    class Meta:
        model= Personas
       
        
   
    
        
        
        fields = [  #aca en esta tupla ponemos los campos del modelo que queremos utilizar

            'fecha_inicio',
            'fecha_final',
            'precio_noche',
            'precio_semana',
            'nonmbre'
          


        ]

        labels ={       # aca en este diccionario pongo las etiqetas que quiero que tengan los textxField en el html
        
        
            'fecha_inicio': 'fecha inicio*',
            'fecha_final': 'fecha final*',
            'precio_noche': 'precio noche*',
            'precio_semana': 'precio semana',
            'nonmbre': 'nombre'
         


        }

        widgets ={ # lo que se va a ver en el formulario del html
           
       
          # 'fecha_inicio': forms.DateTimeInput(format='%d-%m-%Y %H:%M:%S', attrs={'class':'datetimefield'}),
          # 'fecha_final': forms.DateTimeInput(format='%d-%m-%Y %H:%M:%S', attrs={'class':'datetimefield'}), #esta es la clase que puse arriba para que me muestre el calendario
            'precio_noche': forms.NumberInput(),
            'precio_semana': forms.NumberInput(),
         
          'fecha_inicio': DateTimeInput(),
          'fecha_final': DateTimeInput(), # dateTimeINput() viene de la clase de arriba que puse
          'nonmbre': forms.TextInput()
          
           
            #attrs={'class':'form-row'} poner en () ejemplo TextInput() seria la clase de bootdtrap
            #attrs={'placeholder':'Phone Number'} poner esto en el text input en gris pero que se puede escribir arriba de la palabra

        }







