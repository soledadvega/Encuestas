"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#*directorio base

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h-^aaot8(2##*nh!w^o=7g1^iabs#u75wd9k2#y2j!f1uus-p4'
#*clave secreta para hacer encriptaciones de las contraseñas de los usuarios
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
 #*cambie True x False en modo prod.

ALLOWED_HOSTS = []
#poner ip si cambio arriba por modo prod

# Application definition

INSTALLED_APPS = [
    'polls.apps.PollsConfig', #para incluir la aplicacion polls
    'django.contrib.admin',  #sitio administrativo
    'django.contrib.auth',  # sistema de autentificacion
    'django.contrib.contenttypes', #frameworks para tipos de contenido
    'django.contrib.sessions',  #frameworks de sesion de usuario
    'django.contrib.messages',  #frameworks de mensajeria
    'django.contrib.staticfiles',  #frameworks para la gestion de arch estaticos
]

#*personaliza el comportamiento entre el framework,django y la aplic.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#*donde esta la url de mi proy
ROOT_URLCONF = 'mysite.urls'

#*motor de template de django
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

#*es la aplicacion
WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

#*dic donde ponemos la conf de BD
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

#*
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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'es'  #idioma (es) cambio(en-us)

TIME_ZONE = 'UTC'  #uso horario

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/' #permite def. la url para arch. estaticos
#STATIC_ROOT = "/var/www/example.com/static/"   #agregue de testing
