from pathlib import Path
import sys
import os


# Folder settings

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, 'apps'))

# Base settings

SECRET_KEY = 'django-insecure-z+t(esls3*@c_!szcd_r5v=z4b6vbvw4$ioq476oer^(qwnq%y'

DEBUG = True

ALLOWED_HOSTS = []

ROOT_URLCONF = 'settings.urls'

WSGI_APPLICATION = 'settings.wsgi.application'

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Static and media

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# SHELL_PLUS

SHELL_PLUS = "ipython"
SHELL_PLUS_PRINT_SQL = True
SHELL_PLUS_PYGMENTS_FORMATTER_KWARGS = {}
SHELL_PLUS_PRE_IMPORTS = [
    ('django.db', ('connection', 'connections', 'reset_queries')),
    ('datetime', ('datetime', 'timedelta', 'date')),
    ('json', ('loads', 'dumps'))
]
SHELL_PLUS_MODEL_ALIASES = {
    'orders': {
        'Item': 'I',
        'Order': 'O'
    }
}

IPYTHON_KERNEL_DISPLAY_NAME = "Django Shell-Plus"
