from django.db import models
from django_tenants.models import TenantMixin, DomainMixin




class Client(TenantMixin): #hereda de TenantMixin, esta clase Cliente puede tener los campos que yo le quiera agregar
    name = models.CharField(max_length=100)
    paid_until =  models.DateField() # en ingles significa pagado hasta
    is_active = models.BooleanField()  # is_active es por ejemplo si el cliente no paga le desactivo esto en false
    created_on = models.DateField(auto_now_add=True) # me captura el momento del registro en la bbdd

    auto_create_schema = True  #esto es cada ves que creo un cliente me vas a guardar un esquema en la bbdd
    
    def __str__(self):
        return self.name
    
    
    
class Language(models.Model):
    
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=100)    
    
    def __str__(self):
        return self.name
    
    
    
class Domain(DomainMixin):
    
    # is_primary significa si este es el dominio principal del tenant (True) puede tener varios dominios
    pass
