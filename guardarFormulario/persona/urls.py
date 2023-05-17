
from django.urls import path
from  . import views



urlpatterns = [
    path('', views.llenarPlanilla, name= "LLenarPlanilla"),
   


]