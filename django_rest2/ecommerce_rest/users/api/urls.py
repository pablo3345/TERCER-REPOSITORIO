# es un urls como vimos hasta ahora en django comun

from django.urls import path

from users.api.api import UserApiView

urlpatterns = [
    path('usuario/', UserApiView.as_view(), name ='usuarioApi')
]
