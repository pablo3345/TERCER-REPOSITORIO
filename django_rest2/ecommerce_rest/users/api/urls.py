# es un urls como vimos hasta ahora en django comun

from django.urls import path
#from users.api.api import UserApiView
from users.api.api import user_api_view

urlpatterns = [
    #path('usuario/', UserApiView.as_view(), name ='usuarioApi') url basada en clase
    path('usuario/', user_api_view, name ='usuarioApi') # url basada en funcion
]
