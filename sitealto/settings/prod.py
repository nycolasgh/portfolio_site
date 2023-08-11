from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['18.229.27.18','172.31.14.81','altoag.com.br','www.altoag.com.br']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


''' FORMATO PARA USO COM DEPLOY NA PLATAFORMA RAILWAY
DATABASE_URL = os.getenv("DATABASE_URL")

DATABASES = {
    'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=1800),
}
'''

#  FORMATO PARA USO COM DEPLOY NA PLATAFORMA AWS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv("PGDATABASE"),
        'USER': os.getenv("PGUSER"),
        'PASSWORD': os.getenv("PGPASSWORD"),
        'HOST': os.getenv("PGHOST"),
        'PORT': os.getenv("PGPORT"),
    }
}

'''
CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.getenv("CLOUDINARY_URL"),
}
'''


CSRF_TRUSTED_ORIGINS = ["http://ec2-18-229-27-18.sa-east-1.compute.amazonaws.com","http://18.229.27.18","https://altoag.com.br"]

# HTTPS settings

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True

# HSTS settings
SECURE_HSTS_SECONDS = 31536000  # 1 year in seconds
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

