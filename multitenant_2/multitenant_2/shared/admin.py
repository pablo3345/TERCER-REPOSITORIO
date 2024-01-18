

from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from shared.models import Client, Language, Domain

@admin.register(Client)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
        list_display = ('name', 'schema_name', 'paid_until')





admin.site.register(Language) 
admin.site.register(Domain) 