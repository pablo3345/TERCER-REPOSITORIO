from rest_framework.authentication import get_authorization_header # get_authorization_header esta es la funcion que se encuentra en la clase authentication en la documentacion del link del video 27
# la funcion get_authorization_header lo que hace es traernos la variable Authorization auth que viene dentro del header o cabecera, y al enviar la peticion esto se colocaba en la cabecera y podriamos obtener ese token, (fijarme en Postman que aparece header)
# entonces cada interfaz que este conectada tiene que mandar el Authorization con el token para que se proceda a la validacion de todo el sistema
# entonces puedo usar el get_authorization_header para descodificar el token y una vez que lo descodifico obtener el usuario
from users.authtentication import ExpiringTokenAuthentication # me traigo la clase la class...
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

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
         
         #try: # aca hago el try por las dudas de no obtener estos dos valores (user,token) xq sino me da error
         user,token, message = token_expire.authenticate_credentials(token) # cuando hago esto me va hacer todo lo que esta en authenticate_credentials() en authentication
         
         if user != None and token != None:
           return user # lo que quiero aca es el usuario
         
         
         return message # creo que esto seria como el else del if de: if user != None and token != None:
         
        # except:
            # message = token_expire.authenticate_credentials(token) # llamo a la funcion que debe validar este error o excepcion
           
             
     
     
     return None
  
  
  #-------------------------funcion que llamo desde abajo-----------------------------------------------------
    
    # dispatch() es el metodo que toda clase de django ejecuta primero
    def dispatch(self, request, *args, **kwargs):
     
        #ahora desde aqui hago la llamada a la clase ExpiringTokenAuthentication(TokenAuthentication): que se encuentra en authentication
        # lo primero me traigo el token xq la clase ExpiringTokenAuthentication tiene como parametro el token
        
        user = self.get_user(request)
        
        # se encontro un token en la peticion entonces pueden ser dos cosas que nos retorne un message o que nos retorne un usuario
        if user != None:
          if type(user) == str: # esto significa que nos ha retornado un message, fijarme que user hace el llamado de la funcion de arriba  def get_user(self, request):
          
            response= Response({'error':user})
          
            response.accepted_renderer = JSONRenderer()
            response.accepted_media_type ='application/json'
            response.renderer_context = {} # un diccionario vacio xq es un contexto
        
            return response
      
          
          
          
          
          # osea si no me ha retornado un menssage entonces retorname esto, creo que esto seria como un else del if de arriba
          return super().dispatch(request, *args, **kwargs)
   
        response = Response({'error': 'no se han enviado las credenciales'})# esto es si el usuario si es None, seria como un else, recordemos que en la funcion de arriba get_user(request) traigo el token y al descodificarlo me traigo el usuario
          # con esto traigo el token en la funcion de arriba y descodifico el usuario ej:  token = get_authorization_header(request).split()
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type ='application/json'
        response.renderer_context = {} # un diccionario vacio xq es un contexto
        
        return response
      
        
        # todo eso que puse en el response de accepted_renderer etc etc es xq no se puede hacer un solo un Response en una clase como esta que no hereda de APIView, ViewSet etc etc, entonces hay que decirle
     
    