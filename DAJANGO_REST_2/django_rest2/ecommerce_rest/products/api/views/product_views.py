from rest_framework import generics #esta libreria se coloca primero
from base.api import GeneralListApiView #GeneralListApiView seria como una vista de la app base
from products.api.serializers.product_serializers import ProductSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

'''class ProductListAPIViews(GeneralListApiView):# la clase para listar los productos, parece que aca hereda de la vista de la app base GeneralListApiView para mostrar o listar los productos
    
     serializer_class = ProductSerializer'''
     
     
     
class ListProductCreateAPIView(generics.ListCreateAPIView): # vista para crear un producto y listar un producto, aca he unido el listado (get) y la creacion (Post) x eso la vista generica es: (generics.ListCreateAPIView) y antes era solo para crear  (generics.CreateAPIView)
     
     serializer_class= ProductSerializer 
     queryset = ProductSerializer.Meta.model.objects.filter(state=True) # esta consulta la agregue ahora para el metodo de listar y crear (generics.ListCreateAPIView), antes en el metodo solo para crear no tenia esta consulta
     #tambien puedo usar el metodo get_queryset() para la consulta, que es mas escalable, pero para este caso con solo este queryset esta bien
  #------------------------------------------------------------------------------  
  
     # aca si necesito puedo ponerle el metodo def get():
     
     
     def post(self,request): # hago este metodo para personalizarlo, osea para poner mensajes al crear, para que sea mas entendible etc etc
        
        serializer = self.serializer_class(data=request.data)
      
        if serializer.is_valid():
             serializer.save()
             return Response({'message': 'el producto fue creado con exito'},status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # este return seria como el else del if de arriba
   
       
'''class ProductCreateAPIView(generics.CreateAPIView): # vista para crear un producto, la vista de arriba es dos en uno osea listar y crear
     
     serializer_class= ProductSerializer # con esta sola linea de codigo ya me creo el producto con serializer_class= ProductSerializer
  #------------------------------------------------------------------------------   
     def post(self,request): # hago este metodo para personalizarlo, osea para poner mensajes al crear, para que sea mas entendible etc etc
        
        serializer = self.serializer_class(data=request.data)
      
        if serializer.is_valid():
             serializer.save()
             return Response({'message': 'el producto fue creado con exito'},status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # este return seria como el else del if de arriba
   
   
class ProductRetrieveAPIView(generics.RetrieveAPIView): # para listar o traer un producto especifico y desde la url o navegador le paso el id
     
     serializer_class=ProductSerializer
     
     
     def get_queryset(self):
          return self.get_serializer().Meta.model.objects.filter(state=True)# para listar o mostrar un solo producto se debe poner una consulta
     
     
     
class ProductDestroyAPIView(generics.DestroyAPIView):# para eliminar un producto
     
     serializer_class=ProductSerializer
     
     
     def get_queryset(self):
          return self.get_serializer().Meta.model.objects.filter(state=True)# para eliminar un producto se debe poner una consulta
     
     
     
     def delete(self, request, pk=None): # una forma de eliminar un producto pero no de la bbdd sino ocultandolo poniendo state=False
          # aca no uso el metodo updated ya que cambio es estado de state a False, porque si uso updated no me va a permitir hacer esta validacion paso a paso
          product =self.get_queryset().filter(id=pk).first()
          
          if product: # si esta el producto
             product.state=False
             product.save()
             
             return Response({'message': 'Producto eliminado correctamente'},status=status.HTTP_200_OK)
        
          return Response({'error': 'no existe un producto con estos datos'}, status=status.HTTP_400_BAD_REQUEST)# esto seria como el else del if de arriba que dice si hay producto
     

class ProductUpdatedAPIView(generics.UpdateAPIView):
     
     serializer_class=ProductSerializer
     
     def get_queryset(self, pk): # para actualizar tambien tenemos que pasarle un consulta
          # lo que tiene django rest para el UpdateAPIView dos metodos PATCH y PUT, con PATCH obtengo la informacion de la instancia y con PUT para actualizar dicha informacion
          
          return self.get_serializer().Meta.model.objects.filter(state=True).filter(id=pk).first()
       #  return self.get_serializer().Meta.model.objects.filter(state=True)# poniendo esta sola linea en el get_queriset sin el pk, parece que en la interfaz de ayuda ya me aparece el metodo patch y put para actualizar
       # y no hace falta de escribir los dos metodos de abajo patch y put
     
     def patch(self, request, pk=None): # con PATCH obtengo la informacion y con PUT la actualizo
          
         
           if  self.get_queryset(pk):
            
                product_serializer= self.serializer_class(self.get_queryset(pk))
                return Response(product_serializer.data,status=status.HTTP_200_OK)
          
           return Response({'error': 'no existe un producto con estos datos'}, status=status.HTTP_400_BAD_REQUEST) # esto seria como un else del if de arriba, x si no encontro el producto
          
         
     
     def put(self, request, pk=None): # con PATCH obtengo la informacion y con PUT la actualizo
          
            if self.get_queryset(pk):
                 
                  product_serializer= self.serializer_class(self.get_queryset(pk), data = request.data)
                  if product_serializer.is_valid():
                       product_serializer.save()
                       return Response(product_serializer.data,status=status.HTTP_200_OK)
                  
                  return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)# el else del if de arriba
             
             
             
class ProductUpdateRetrieveAPIView(generics.RetrieveUpdateAPIView): # para listar o traer un producto especifico y actualizar un producto
     
     serializer_class=ProductSerializer
     
     
     def get_queryset(self): # en este caso la consulta es un get, para traer el produycto
          return self.get_serializer().Meta.model.objects.filter(state=True)# para listar o mostrar un solo producto se debe poner una consulta
     
     
     
     # aca puedo sobreescribir el metodo put osea cuango actualizo
     # def put(self, request, pk=None):'''
          
       
     
     
class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):# me sirve para traer actualizar y eliminar un producto
     
     serializer_class=ProductSerializer
     
     
     def get_queryset(self, pk=None):
          
          if pk==None:
          
           return self.get_serializer().Meta.model.objects.filter(state=True)
      
          else:
           return self.get_serializer().Meta.model.objects.filter(state=True).filter(id=pk).first()
               
     
          
    
     def patch(self, request, pk=None): # con PATCH obtengo la informacion y con PUT la actualizo
          
         
           if  self.get_queryset(pk):
            
                product_serializer= self.serializer_class(self.get_queryset(pk))
                return Response(product_serializer.data,status=status.HTTP_200_OK)
          
           return Response({'error': 'no existe un producto con estos datos'}, status=status.HTTP_400_BAD_REQUEST) # esto seria como un else del if de arriba, x si no encontro el producto
          
         
     
     def put(self, request, pk=None): # con PATCH obtengo la informacion y con PUT la actualizo
          
            if self.get_queryset(pk):
                 
                  product_serializer= self.serializer_class(self.get_queryset(pk), data = request.data)
                  if product_serializer.is_valid():
                       product_serializer.save()
                       return Response(product_serializer.data,status=status.HTTP_200_OK)
                  return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)# el else del if de arriba
     
     def delete(self, request, pk=None): # una forma de eliminar un producto pero no de la bbdd sino ocultandolo poniendo state=False
          # aca no uso el metodo updated ya que cambio es estado de state a False, porque si uso updated no me va a permitir hacer esta validacion paso a paso
          product =self.get_queryset().filter(id=pk).first()
          
          if product: # si esta el producto
             product.state=False
             product.save()
             
             return Response({'message': 'Producto eliminado correctamente'},status=status.HTTP_200_OK)
        
          return Response({'error': 'no existe un producto con estos datos'}, status=status.HTTP_400_BAD_REQUEST)# esto seria como el else del if de arriba que dice si hay producto
     
    
     
 # ENTONCES PARA SIMPLIFLICAR EL SOFTWARE DEJAMOS SOLO DOS FUNCIONES QUE HACEN TODO EL CRUD DE LISTAR, CREAR, ACTUALIZAR Y ELIMINAR
 
 # en el video 24 unifico todas estas vistas    
 
 
 
 #----------------ahora hago una sola clase viewsets que me hace todo el CRUD, con todos los metodos HTTP--------------------------------
 
class ProductViewSet(viewsets.ModelViewSet): # hay varios viewset en este caso uso (viewsets.ModelViewSet):
     
     serializer_class=ProductSerializer
    # queryset= ProductSerializer.Meta.model.objects.filter(state=True)
     
#-----con lo de arriba ya me genera todos los metodos en la interfaz de ayuda, ahora puedo sobreescribir todos los metodos

    
     def get_queryset(self, pk=None):
          
          if pk==None:
          
           return self.get_serializer().Meta.model.objects.filter(state=True)
      
          else:
           return self.get_serializer().Meta.model.objects.filter(state=True).filter(id=pk).first()
      
     
     def list(self, request): # el listado de todos los productos
         # print("hola desde el listado")
          product_serializer= self.get_serializer(self.get_queryset(), many=True)
          
          return Response(product_serializer.data, status= status.HTTP_200_OK)
          
          
      
      
     def create(self,request): # este seria el post para guardar, pero en viewsets.ModelViewSet se reemplaza por el create
        
        serializer = self.serializer_class(data=request.data)
      
        if serializer.is_valid():
             serializer.save()
             return Response({'message': 'el producto fue creado con exito'},status=status.HTTP_201_CREATED)
                    
     
     def destroy(self, request, pk=None): # una forma de eliminar un producto pero no de la bbdd sino ocultandolo poniendo state=False
          # aca no uso el metodo updated ya que cambio es estado de state a False, porque si uso updated no me va a permitir hacer esta validacion paso a paso
          # en viewsets.ModelViewSet el metodo no se llama delete sino destroy
          product =self.get_queryset().filter(id=pk).first()
          
          if product: # si esta el producto
             product.state=False
             product.save()
             
             return Response({'message': 'Producto eliminado correctamente'},status=status.HTTP_200_OK)
        
          return Response({'error': 'no existe un producto con estos datos'}, status=status.HTTP_400_BAD_REQUEST)# esto seria como el else del if de arriba que dice si hay producto
     
      
     
     def update(self, request, pk=None): # antes este metodo era el put pero con viewsets.ModelViewSet se llama update
          
            if self.get_queryset(pk):
                 
                  product_serializer= self.serializer_class(self.get_queryset(pk), data = request.data)
                  if product_serializer.is_valid():
                       product_serializer.save()
                       return Response(product_serializer.data,status=status.HTTP_200_OK)
                  return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)# el else del if de arriba
     