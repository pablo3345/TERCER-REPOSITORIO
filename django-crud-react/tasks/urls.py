from django.urls import path, include
from rest_framework.documentation import include_docs_urls # para documentar la informacion
from rest_framework import routers
from tasks import views

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskView, 'tasks')



urlpatterns = [
    
    path("api/v1/", include(router.urls)), # v1 significa version 1, por si hay cambios en la aplicacion
    path("docs/", include_docs_urls(title="Tasks API"))
]

#todas estas rutas de aqui ya estan generando las rutas, GET, PUT, POST DELETE