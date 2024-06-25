from base.api import GeneralListApiView #GeneralListApiView seria como una vista de la app base
from products.api.serializers.product_serializers import ProductSerializer


class ProductListAPIViews(GeneralListApiView):# la clase para listar los productos, parece que aca hereda de la vista de la app base GeneralListApiView para mostrar o listar los productos
    
     serializer_class = ProductSerializer
     
     
  