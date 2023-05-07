from django.contrib import admin
from .models import Personas
# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ("fecha_inicio", "fecha_final","precio_noche", "precio_semana", "created", "updated")
 







admin.site.register(Personas, PersonaAdmin)


