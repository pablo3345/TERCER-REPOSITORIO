from rest_framework.authentication import TokenAuthentication # aca me traigo la clase TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from datetime import timedelta
from django.utils import timezone
from django.conf import settings


class ExpiringTokenAuthentication(TokenAuthentication): # esto es para agregar un tiempo de expiracion al token
    
    expired =False # me creo una variable que esta en False y cuando entra al  token_expire_handler(self, token): estara en True, para decirle que ha expirado, creo que do dijo para avisarme al front end
    # y al final la retorno en el return de def authenticate_credentials(self, key):
    
    
    #---------------------funcion-----------------------------------------------------------------
    # expires_in = expira en
    def expires_in(self, token): # este metodo va decir cual es el tiempo que ha pasado, realiza todo el calculo
      
    #time elapsed = tiempo transcurrido
     time_elapsed = timezone.now() - token.created # la clase Token tiene un campo que es la fecha de creacion seria created, esto seria el tiempo transcurrido, el tiempo que ha pasado
     
     #left time = tiempo restante
     left_time= timedelta(seconds=settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed # el resultado de arriba nos va a dar el tiempo que falta, por eso le resto time_elapsed
     # en el setting me cree una variable que dice cunato tiempo quiero que expire TOKEN_EXPIRED_AFTER_SECONDS =
     return left_time # left_time es tiempo que falta
     
   #----------------------funcion----------------------------------------------------------------- 
    #  is_token_expired = ¿el token ha caducado?
    def is_token_expired(self, token): # esta funcion me pregunta si el token a expirado, realiza la comparacion
     
     return self.expires_in(token) <  timedelta(seconds=0)# aca pregunta si la fecha de expiracion del token es menor a la hora actual,  self.expires_in(token) es la funcion de arriba
   #----------------------funcion----------------------------------------------------------------- 
    #  token_expire_handler = controlador de caducidad de token
    def token_expire_handler(self, token):
      
      is_expire =self.is_token_expired(token) # is_expire es la variable para saber si el token ha expirado
      
      if is_expire:
         self.expired=True
         print("su token correspondiente ha expirado")
         user = token.user
         token.delete() # como ya a expirado el token te lo eliminio y te creo uno nuevo, te lo actualizo
         
         # aca prodria poner que me elimine la sesion tambien, pero en este ecommrce no lo vamos a hacer
         
         token = self.get_model().objects.create(user = user) # aca creo un nuevo token, se lo estoy refrescando
        
      return is_expire, token
      
   #----------------------funcion-----------------------------------------------------------------  
   
    def authenticate_credentials(self, key): # que es la clave que seria el token
    # esta es la clase que ejecuta todo lo demas
    
       message,user,token = None, None, None # cuando el message ha sido None significa qyue todo ha salido correcto, osea no entra a los message de abajo
       try:  
        
         token = self.get_model().objects.select_related('user').get(key=key)# aca me traigo el token y get_model() seria la funcion que esta dentro de la clase TokenAuthentication que trata todo el tema de autenticacion  y que dicha funcion devuelve el token
         # aca al toquen tambien puedo obtenerlo de la forma tradicional sin get_model()
         # select_related('user') es para que nos traiga la instancia mas eficiente, ('user') estaria dentro de la relacion y asi poder traerlo mas optimizado despues
         
         user=token.user # aca ya encontro el usuario
       except self.get_model().DoesNotExist: # DoesNotExist seria la excepcion que tiene la funcion get_model() dentro de la clase TokenAuthentication, que dicha documentacion se encuentra creo que en un link en los comentarios del video 27
           
          #raise AuthenticationFailed('token invalido') # esta es la clase de excepcion, pero sale un error 500 y dijo que a los errores 500 en esta ocacion hay que evitarlos para que no se detenga la ejecucion
          message="token invalido"
          #return message # el mensaje de token invalido para que no se me detenga la ejecusion con el error 500
          
          self.expired=True # puede que tu token haya expirado
        
       if token is not None:
        
          if not token.user.is_active:
              # raise AuthenticationFailed('usuario no activo o eliminado') # esta es la clase de excepcion
               message="usuario no activo o eliminado"
              # return message  # el mensaje de token invalido para que no se me detenga la ejecusiuon con el error 500
             
          is_expired = self.token_expire_handler(token) # is_expired es si el token ha expirado y token_expire_handeler(token) es la funcion que llamo y esta arriba
       
          if is_expired:
        # raise AuthenticationFailed('su token ha expirado')
            message="su token ha expirado"
        # return message  # el mensaje de token invalido para que no se me detenga la ejecusion con el error 500
       
       
       return(user, token, message, self.expired)
     
     
     # con todo esto le hemos dado un tiempo de vida a nuestro token, ahora tenemos que implementarlo
     
     
     
     
   