# es un urls como vimos hasta ahora en django comun

from django.urls import path

from products.api.views.general_views import MeasureUnitListAPIView, CategoryProductListAPIView, IndicadorListAPIView
from products.api.views.product_views import ProductListAPIViews


urlpatterns = [
    path('measure_unit/', MeasureUnitListAPIView.as_view(), name ='measure_unit'), # aca en django rest framework se pone asi, son generales y todo se manaje por los metodos get, post, put, delete
    path('category_Product/', CategoryProductListAPIView.as_view(), name ='category_Product'),
    path('indicator/', IndicadorListAPIView.as_view(), name ='indicator'),
    path('product/', ProductListAPIViews.as_view(), name ='product')

]
