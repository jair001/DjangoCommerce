"""
Django settings for config project.
se cambia x settings ya que usa .env
"""
import os   # lee donde está el sistema operativo
from dotenv import load_dotenv  # lea de .env
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)   # todas las variables lea de este path

# SECRET_KEY = 'django-insecure-7jg$e@y*-53t5xls#9893-k+h00%k3if1t+e)#i!)l4_f2ze)z'
SECRET_KEY = os.getenv("SECRET_KEY")

# DEBUG = True
DEBUG = os.getenv("DEBUG")

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # THIRD APPS
    # 'import_export',
    'crispy_forms',

    # LOCAL APPS
    'catalogue.apps.CatalogueConfig',
    'customers.apps.CustomersConfig',
    'users',
    'orders'
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'config/templates'
        ],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'DjangoCommerce',
        'HOST': 'localhost',
        'USER': 'postgres',
        'PASSWORD': 'Jesp406'
    }
}
'''
DATABASES = {
    'default': {
        'ENGINE': os.getenv("SQL_ENGINE"),
        'NAME': os.getenv("SQL_DATABASE"),
        'HOST': os.getenv("SQL_HOST"),
        'USER': os.getenv("SQL_USER"),
        'PASSWORD': os.getenv("SQL_PASSWORD")
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Guayaquil'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
# print(BASE_DIR / "static")
PATH_STATIC = BASE_DIR / "config/static"
STATICFILES_DIRS = [
    str(PATH_STATIC)
]
print(STATICFILES_DIRS)
# STATIC_ROOT = BASE_DIR / 'config/static'
# print(STATIC_ROOT)

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
# print(MEDIA_ROOT)

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# EMAILs
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'