"""
Local development settings for Sulleys project.
This file overrides production settings for local development.
"""
import os

# Set dummy environment variables before importing settings
# This prevents KeyError when settings.py tries to access them
os.environ.setdefault('CLOUDINARY_URL', 'cloudinary://dummy:dummy@dummy')
os.environ.setdefault('SECRET_KEY', 'local-development-secret-key')
os.environ.setdefault('DATABASE_URL', 'postgres://backend:backend@localhost:5432/backend')

from .settings import *

# Enable debug mode for local development
DEBUG = True

# Local development hosts
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0', '*']

# Local development secret key
SECRET_KEY = os.environ.get('SECRET_KEY', 'local-development-secret-key-not-for-production')

# Disable django-heroku for local development
# (This prevents it from overriding our local settings)
import sys
if 'django_heroku' in sys.modules:
    del sys.modules['django_heroku']

# Database configuration for local Docker PostgreSQL
# Override any database settings from django-heroku
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'backend',
        'USER': 'backend',
        'PASSWORD': 'backend',
        'HOST': 'localhost',
        'PORT': '5432',
        'CONN_MAX_AGE': 0,  # Disable connection pooling for local development
    }
}

# DISABLE CLOUDINARY - Use local file storage instead
INSTALLED_APPS = [app for app in INSTALLED_APPS if app not in ['cloudinary', 'cloudinary_storage']]

# Local file storage settings
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Use local file storage instead of Cloudinary
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
THUMBNAIL_DEFAULT_STORAGE = 'django.core.files.storage.FileSystemStorage'

# Static files for local development
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# Create media directory if it doesn't exist
os.makedirs(MEDIA_ROOT, exist_ok=True)
os.makedirs(STATIC_ROOT, exist_ok=True)

# Simple logging for local development
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}

print("🚀 Using local development settings - Cloudinary disabled, using local storage") 