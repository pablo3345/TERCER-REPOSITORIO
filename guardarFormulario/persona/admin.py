from django.contrib import admin
from .models import Personas
# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ("nombre", "apellido", "direccion", "telefono", "codigo_postal", "created", "updated")
    radio_fields = {'sexo': admin.VERTICAL}







admin.site.register(Personas, PersonaAdmin)


