
from django.urls import path
from  persona import views



urlpatterns = [
    path('', views.llenarPlanilla, name= "LLenarPlanilla"),


]