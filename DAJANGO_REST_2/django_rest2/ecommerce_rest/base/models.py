from django.db import models
#from simple_history.models import HistoricalRecords # esta libreria es para saber todo el historial del usuario (hay que instalarla en la consola)
# Create your models here.


class BaseModel(models.Model): # creamos el modelo base que ahora en adelante lo vamos a usar en todos los modelos
    """Model definition for BaseModel."""

    # todo: Define fields here
    id = models.AutoField(primary_key = True)
    state = models.BooleanField('Estado',default = True)
    created_date = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)
    modified_date = models.DateField('Fecha de Modificación', auto_now=True, auto_now_add=False)
    deleted_date = models.DateField('Fecha de Eliminación', auto_now=True, auto_now_add=False)
 
 
    class Meta:
        """Meta definition for BaseModel."""
        abstract = True # es abstract xq es el modelo, base osea otros modelos heredan de este
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos Base'
