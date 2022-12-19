from .base import *
import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASE_URL = os.getenv("DATABASE_URL")

DATABASES = {
    'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=1800),
}

CSRF_TRUSTED_ORIGINS = ['https://web-production-1c31.up.railway.app']


