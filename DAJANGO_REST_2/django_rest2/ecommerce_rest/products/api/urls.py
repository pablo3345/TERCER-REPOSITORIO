# es un urls como vimos hasta ahora en django comun

from django.urls import path

#from products.api.views.general_views import MeasureUnitListAPIView, CategoryProductListAPIView, IndicadorListAPIView
#from products.api.views.product_views import ProductListAPIViews,  ListProductCreateAPIView, ProductRetrieveAPIView, ProductDestroyAPIView, ProductUpdatedAPIView, ProductCreateAPIView, ProductUpdateRetrieveAPIView, ProductRetrieveUpdateDestroyAPIView
from products.api.views.product_views import  ListProductCreateAPIView, ProductRetrieveUpdateDestroyAPIView


urlpatterns = [
   # path('measure_unit/', MeasureUnitListAPIView.as_view(), name ='measure_unit'), # aca en django rest framework se pone asi, son generales y todo se manaje por los metodos get, post, put, delete
   # path('category_Product/', CategoryProductListAPIView.as_view(), name ='category_Product'),
   # path('indicator/', IndicadorListAPIView.as_view(), name ='indicator'),
    
    #----------------------------------------------------------------------------------------------
    
   # path('product/list/', ProductListAPIViews.as_view(), name ='product_List'),
   # path('product/create/',  ProductCreateAPIView.as_view(), name ='product_Create'),
   # path('product/retrive/<int:pk>/',  ProductRetrieveAPIView.as_view(), name ='product_retrieve'),
   # path('product/destroy/<int:pk>/',  ProductDestroyAPIView.as_view(), name ='product_destroy'),
   # path('product/updated/<int:pk>/',  ProductUpdatedAPIView.as_view(), name ='product_updated'),
    path('product/',  ListProductCreateAPIView.as_view(), name ='product'), # esta url corresponde a la vista para listar (get) y crear un producto (post), por eso se llama ListProductCreateAPIView, aca tengo dos en uno y no tengo que hacer dos vistas por separado
   # path('product/retrive_update/<int:pk>/',  ProductUpdateRetrieveAPIView.as_view(), name ='product_retrieve_update'),
    path('product/retrive_update_destroy/<int:pk>/',  ProductRetrieveUpdateDestroyAPIView.as_view(), name ='product_retrieve_update_destroy') #esta url sirve para traer, editar o eliminar un producto

]
