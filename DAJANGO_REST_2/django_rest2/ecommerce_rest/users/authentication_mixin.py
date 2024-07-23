from rest_framework import status
from rest_framework.authentication import get_authorization_header # get_authorization_header esta es la funcion que se encuentra en la clase authentication en la documentacion del link del video 27
# la funcion get_authorization_header lo que hace es traernos la variable Authorization auth que viene dentro del header o cabecera, y al enviar la peticion esto se colocaba en la cabecera y podriamos obtener ese token, (fijarme en Postman que aparece header)
# entonces cada interfaz que este conectada tiene que mandar el Authorization con el token para que se proceda a la validacion de todo el sistema
# entonces puedo usar el get_authorization_header para descodificar el token y una vez que lo descodifico obtener el usuario
from users.authtentication import ExpiringTokenAuthentication # me traigo la clase la class...
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

class Authentication(object):
  
    user =None
    user_token_expire = False
   
    
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
         user,token, message, self.user_token_expire = token_expire.authenticate_credentials(token) # cuando hago esto me va hacer todo lo que esta en authenticate_credentials() en authentication
         # si ha expirado o no, lo voy a guardar en esta variable self.user_token_expire
         
         if user != None and token != None:
           self.user = user # si paso este if significa que hay un usuario, para poder usuarlo en cualquier clase, cualquier vista, para validar cualquier cosa
           
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
          if type(user) == str: #si entra a este if significa que va haber un message de error, por ej: el token haya expirado, o el usuario este desactivado dependiendo de cual sea el usuario
            # esto significa que nos ha retornado un message, fijarme que user hace el llamado de la funcion de arriba  def get_user(self, request):
          
            response= Response({'error':user,'expired':self.user_token_expire}, status = status.HTTP_400_BAD_REQUEST) # 401 no autorizado
              # 'expired':self.user_token_expire le mando esto para saber en el front end si el token expiro
              #'error': user, es el mensaje como tal, xq aca pregunto si esto es un mensaje  if type(user) == str:
            response.accepted_renderer = JSONRenderer()
            response.accepted_media_type ='application/json'
            response.renderer_context = {} # un diccionario vacio xq es un contexto
        
            return response
      
          
          if  not self.user_token_expire: # siempre que el token esta vencido o ya cambio de toquen, entonces no me va a pintar nada, por eso le puse el return
             print("entro al if raro")
             return super().dispatch(request, *args, **kwargs)
          
     
             
       
        response = Response({'error': 'no se han enviado las credenciales','expired':self.user_token_expire}, status=status.HTTP_400_BAD_REQUEST)# esto es si el usuario si es None, seria como un else, recordemos que en la funcion de arriba get_user(request) traigo el token y al descodificarlo me traigo el usuario
        # si el usuario es None es xq no se ha enviado un token en la peticion x eso no se han enviado las credenciales
          # con esto traigo el token en la funcion de arriba y descodifico el usuario ej:  token = get_authorization_header(request).split()
          # 'expired':self.user_token_expire le mando esto para saber en el front end si el token expiro
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type ='application/json'
        response.renderer_context = {} # un diccionario vacio xq es un contexto
        print("hola")
        return response
      
        
        # todo eso que puse en el response de accepted_renderer etc etc es xq no se puede hacer un solo un Response en una clase como esta que no hereda de APIView, ViewSet etc etc, entonces hay que decirle
     
      # probando yo en el postman cuando le mando el toquen vencido, no encuentra el usuario y me envia 'error': 'no se han enviado las credenciales', pero
      # la segunda vez al apretar el boton send, si encuentra el usuario xq tiene un nuevo toquen y le al enviarle el vencido me manda al message "token invalido"
    