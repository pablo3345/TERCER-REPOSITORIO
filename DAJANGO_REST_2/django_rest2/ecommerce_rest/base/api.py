from rest_framework import generics

# esto seria como una vista creo

class GeneralListApiView(generics.ListAPIView):
    # hago esto para no tener que hacer en la vista de producto 3 vistas que me retorne lo mismo, con este metodo generalizo esas tres vistas
    serializer_class=None
    
    def get_queryset(self): # esta funcion si s si tiene este nombre y no otro
        
        model = self.get_serializer().Meta.model #get_serializer().Meta.model yo se que en los serializadores cada modelSerializer tiene una clase Meta con el modelo, bueno aca los generalizo a todos y no los pongo
      
        return model.objects.filter(state=True)
    
    
    
    # cdrf.co pagina con documentacion buena de REST
    

