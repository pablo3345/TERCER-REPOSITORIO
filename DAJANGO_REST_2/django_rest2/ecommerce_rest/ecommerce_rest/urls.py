"""
URL configuration for ecommerce_rest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path, include


# importar swagger, aparece toda la documentacion en la pagina de swagger, el link esta en el video 26
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
#--------------------------------------------------
from users.views import Login, Logaut, UserToken





schema_view = get_schema_view(
   openapi.Info(
      title="Documentacion de API",
      default_version='v0.1',
      description="Documentacion publica de api ecommerce",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="pabloandresperuchi@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   
    # agrego las rutas de swagger para ver las distintas interfaz que brinda esta libreria
    re_path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   
   # ----------------------------------------------------------------
    path('admin/', admin.site.urls),
    path('usuario/', include('users.api.urls')),
    path('products_1/', include('products.api.urls')),
    path('products_2/', include('products.api.routers')),# la url de los viewSet
    path('', Login.as_view(), name='Login'),
    path('logaut/', Logaut.as_view(), name='Logaut'),
    path('refresh-token/', UserToken.as_view(), name='refresh-token')
]

