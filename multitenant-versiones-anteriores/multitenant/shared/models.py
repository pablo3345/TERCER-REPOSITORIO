from django.db import models
from tenant_schemas.models import TenanMixin
#from django_tenants.models import TenantMixin

# Create your models here.

#los modelos que esten aqui van a ser comprtidas x todos los clientes

class Client(TenantMixin): #hereda de TenantMixin
    
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True) # is_active es por ejemplo si el cliente no paga le desactivo esto en false
    create_on = models.DateField(auto_now_add=True) # me captura el momento del registro en la bbdd
    auto_create_schema=True #esto es cada ves que creo un cliente me vas a guardar un esquema en la bbdd
    
    def __str__(self):
        return self.name
    
class Language(models.Model):
    
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=100)    
    
    def __str__(self):
        return self.name
    
    
    
