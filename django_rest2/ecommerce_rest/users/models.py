from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from simple_history.models import HistoricalRecords # esta libreria es para saber todo el historial del usuario (hay que instalarla en la consola)


class UserManager(BaseUserManager):
    def _create_user(self, username, email, name,last_name, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            email = email,
            name = name,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, name,last_name, password=None, **extra_fields): # sirve para crear usuarios normales
        return self._create_user(username, email, name,last_name, password, False, False, **extra_fields)

    def create_superuser(self, username, email, name,last_name, password=None, **extra_fields):# sirve para crear superusuarios
        return self._create_user(username, email, name,last_name, password, True, True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin): # es un usuario comun y corriente personalizado
    #Por lo tanto, al declarar class User(AbstractBaseUser, PermissionsMixin):, estás creando un modelo de usuario personalizado 
    # que tiene todas las funcionalidades básicas de un usuario, además de la capacidad de manejar roles y permisos. Esto es útil
    # si necesitas agregar campos adicionales al modelo de usuario o cambiar el comportamiento del modelo de usuario predeterminado.
    username = models.CharField(max_length = 255, unique = True)
    email = models.EmailField('Correo Electrónico',max_length = 255, unique = True,)
    name = models.CharField('Nombres', max_length = 255, blank = True, null = True)
    last_name = models.CharField('Apellidos', max_length = 255, blank = True, null = True)
    image = models.ImageField('Imagen de perfil', upload_to='perfil/', max_length=255, null=True, blank = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    historical = HistoricalRecords() # el historial del usuario, todo lo que afecte al modelo usuario se va a guardar aqui
    objects = UserManager()# con esto objects puedo llamar a los metodos de arriba def create_user, def create_superuser

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','name','last_name'] # parece que con esto cuando creo el superusuario en la consola de python me pidel ademas el nombre y apoellido

    def __str__(self):
        return f'{self.name} {self.last_name}'
 
 
 