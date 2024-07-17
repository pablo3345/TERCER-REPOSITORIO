from rest_framework.authentication import get_authorization_header # get_authorization_header esta es la funcion que se encuentra en la clase authentication en la documentacion del link del video 27
# la funcion get_authorization_header lo que hace es traernos la variable Authorization auth que viene dentro del header o cabecera, y al enviar la peticion esto se colocaba en la cabecera y podriamos obtener ese token, (fijarme en Postman que aparece header)
# entonces cada interfaz que este conectada tiene que mandar el Authorization con el token para que se proceda a la validacion de todo el sistema
# entonces puedo usar el get_authorization_header para descodificar el token y una vez que lo descodifico obtener el usuario
from users.authtentication import ExpiringTokenAuthentication # me traigo la clase la class...

class Authentication(object):
    
    def get_user(self, request): # hago esta funcion para llamarla desde dispatch, la hago para no hacer todo junto en dispatch
     token = get_authorization_header(request).split() # el split() aparentemente divide una cadena de texto en partes mas pequeñas por ejemplo en una lista ["la", "lluvia", "es", "linda"]
     if token:
         try:
          token = token[1].decode() # accedo a la posicion 1 porque es el tokem ej sdfsgzgaegaregag , y la posicion 0 es la palabra token
         
    
         except:
          
          return None # si no hay token, no me da error, xq aca le puse que me retorne none
      
      
         #----si todo salio bien en el try de arriba, entonces ejecutame este codigo------
         
         token_expire = ExpiringTokenAuthentication() # para ver si mi token expiro llamando a la funcion
         
         try: # aca hago el try por las dudas de no obtener estos dos valores (user,token) xq sino me da error
           user,token = token_expire.authenticate_credentials(token) # cuando hago esto me va hacer todo lo que esta en authenticate_credentials() en authentication
         
         
         except:
             message = token_expire.authenticate_credentials(token) # llamo a la funcion que debe validar este error o excepcion
           
             
     
     
     return None
  
  
  #-------------------------funcion que llamo desde abajo-----------------------------------------------------
    
    # dispatch() es el metodo que toda clase de django ejecuta primero
    def dispatch(self, request, *args, **kwargs):
     
        #ahora desde aqui hago la llamada a la clase ExpiringTokenAuthentication(TokenAuthentication): que se encuentra en authentication
        # lo primero me traigo el token xq la clase ExpiringTokenAuthentication tiene como parametro el token
        
        user = self.get_user(request)
        
        
        
        return super().dispatch(request, *args, **kwargs)
   
        
        
        
        
        
    