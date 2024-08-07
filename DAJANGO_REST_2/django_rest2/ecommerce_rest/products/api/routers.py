from rest_framework.routers import DefaultRouter # DefaultRouter nos va a permitir crear rutas automaticas dependiendo el viewsSet que utilicemos
from products.api.views.product_views import ProductViewSet # me traigo la vista a igual que en el urlpatterns con las urls
from products.api.views.general_views import *

router = DefaultRouter() # creo la variable router

router.register(r'productos', ProductViewSet, basename='productos') # como las url de los viewSets no se ponen como en los otros casos, aca le pongo el nombre de la url que quiero que se muestre en el navegador, seria (product/)
# poniendo /1/ que es el producto con si id, en la interfaz de ayuda ya me aparecen los metodos delete, update etc

router.register(r'measure-unit', MeasureUnitViewSet, basename='measure_unit') 
router.register(r'category-products', CategoryProductViewSet, basename='category_products')
router.register(r'indicators', IndicadorViewSet, basename='indicators') 


urlpatterns = router.urls # la variable routers va ser la encargada de las rutas



