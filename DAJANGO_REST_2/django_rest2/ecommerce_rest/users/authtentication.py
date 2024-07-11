from rest_framework.authentication import TokenAuthentication # aca me traigo la clase TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from datetime import timedelta
from django.utils import timezone
from django.conf import settings


class ExpiringTokenAuthentication(TokenAuthentication): # esto es para agregar un tiempo de expiracion al token
    
    
    def expires_in(self, token): # este metodo va decir cual es el tiempo que ha pasado, realiza todo el calculo
      
     time_elapsed = timezone.now - token.created # la clase Token tiene un campo que es la fecha de creacion seria created, esto seria el tiempo transcurrido, el tiempo que ha pasado
     left_time= timedelta(seconds=settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed # el resultado de arriba nos va a dar el tiempo que falta, por eso le resto time_elapsed
     # en el setting me cree una variable que dice cunato tiempo quiero que expire TOKEN_EXPIRED_AFTER_SECONDS =
     return left_time # left_time es tiempo que falta
     
   #----------------------funcion----------------------------------------------------------------- 
   
    def is_token_expired(self, token): # esta funcion me pregunta si el token a expirado, realiza la comparacion
     
     return self.expires_in(token) <  timedelta(seconds=0)# aca pregunta si la fecha de expiracion del token es menor a la hora actual,  self.expires_in(token) es la funcion de arriba
   #----------------------funcion----------------------------------------------------------------- 
   
    def token_expire_handler(self, token):
      
      is_expire =self.is_token_expired(token) # is_expire es la variable para saber si el token ha expirado
      
      if is_expire:
        print('token expirado')
        
      return is_expire
      
   #----------------------funcion-----------------------------------------------------------------  
   
    def authenticate_credentials(self, key): # que es la clave que seria el token
    
       try:  
        
         token = self.get_model.objects.select_related('user').get(key=key)# aca me traigo el token y get_model() seria la funcion que esta dentro de la clase TokenAuthentication que trata todo el tema de autenticacion  y que dicha funcion devuelve el token
         # aca al toquen tambien puedo obtenerlo de la forma tradicional sin get_model()
         # select_related('user') es para que nos traiga la instancia mas eficiente, ('user') estaria dentro de la relacion y asi poder traerlo mas optimizado despues
         

       except self.get_model().DoesNotExist: # DoesNotExist seria la excepcion que tiene la funcion get_model() dentro de la clase TokenAuthentication, que dicha documentacion se encuentra creo que en un link en los comentarios del video 27
           
           raise AuthenticationFailed('token invalido') # esta es la clase de excepcion
        
        
       if not token.user.is_active:
               raise AuthenticationFailed('usuario no activo o eliminado') # esta es la clase de excepcion
             
             
       is_expired = self.token_expire_handler(token) # is_expired es si el token ha expirado y token_expire_handeler(token) es la funcion que llamo y esta arriba
       
       if is_expired:
         raise AuthenticationFailed('su token ha expirado')
       
       
       return(token.user, token)
     
     
     # con todo esto le hemos dado un tiempo de vida a nuestro token, ahora tenemos que implementarlo