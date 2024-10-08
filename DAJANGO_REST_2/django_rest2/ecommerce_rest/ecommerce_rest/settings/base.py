"""
Django settings for ecommerce_rest project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#s4(c#n61jvpqk3pyd^ko(s9o#l45m=j6i^f2#pm!p011-#hol' # es una clave secreta unica, encriptada que tiene cada proyecto de django que sirven para la implementacion de token

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
BASE_APPS = [# aplicaciones bases las que vienen por defecto
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


# las aplicaciones mias las que yo creo
LOCAL_APPS=[
    'users',
    'base',
    'products',
    
    
    
]


#aplicaciones de terceros que son las librerias externas basicamente
THIRD_APPS=[
  
    'corsheaders',# esta libreria me la instale en la consola, y sirve para tema de polica y seguridad
    'rest_framework',
    'rest_framework.authtoken', # esto lo unico que vamos a colocar para el token de autenticacion, por eso necesito hacer un python manage.py migrate, no hago un makemigrations xq me aparece que no hay cambios detectedos
    'simple_history', # esta libreria que es la que me instale para ver el historial del usuario, es de terceros x eso se coloca aqui
    'drf_yasg', # la libreria swagger
    
]

INSTALLED_APPS = BASE_APPS + LOCAL_APPS+ THIRD_APPS


SWAGGER_SETTINGS={'DOC_EXPANSION': 'none'} # para que en la interfaz swagger no me muestre todos los metodos uno abajo del otro y yo seleccione para verlos


TOKEN_EXPIRED_AFTER_SECONDS = 900 # me creo una variable para que me diga cuanto tiempo quiero que expire el token, generalmente son 15 minutos que serian 900 segundos

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # aca coloco el corsheders en el moddleware y en la documentacion dice que se coloca lo mas arriba posible
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware', 
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware', # coloco esto para saber a que usuario hace referencia a cada cambio en el modelo, el historial
]

ROOT_URLCONF = 'ecommerce_rest.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecommerce_rest.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True

USE_TZ = True


CORS_ALLOWED_ORIGINS =["http://localhost:3000"] # esto es una configuracion que nos dice a nuestro backend de donde permitimos peticiones,
# y en este caso le digo que me lo permita pero en el localhost 3000, esta es la ip de local, estariamos en produccion iria la ip correspondiente
# creo que dijo que mediante este cors se pueden hacer peticiones desde react, desde aplicaciones android, javascript
CORS_ORIGIN_WHITELIST= ["http://localhost:3000"]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
AUTH_USER_MODEL ='users.User' # con esto le digo a django que mi aplicacion va a funcionar con un modelo llamado usuario

#STATICFILES_DIRS = [os.path.join(BASE_DIR, 'frontend', 'build', 'static')]  # importe esto del tutorial para conectar django con react
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = '/static/'