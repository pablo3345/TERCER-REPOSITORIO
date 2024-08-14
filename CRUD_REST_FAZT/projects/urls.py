from rest_framework import routers # los viewSet trabajan con routers
from .api import ProjectViewsets

routers= routers.DefaultRouter() # esto seria todo lo del crud y me lo vas a guardar en una variable routers

routers.register('api/projects',ProjectViewsets, 'project')

urlpatterns = routers.urls
    
