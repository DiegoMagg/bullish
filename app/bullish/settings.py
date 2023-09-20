from os import environ, path

from bullish.default_settings import *

# Static files

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

STORAGES = {
    'default': {
        'BACKEND': 'whitenoise.storage.CompressedStaticFilesStorage',
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedStaticFilesStorage',
    }
}

STATIC_URL = '/static/'

STATIC_ROOT = path.join(BASE_DIR, 'staticfiles')

# Celery

CELERY_BROKER_URL = environ.get('CELERY_BROKER_URL', 'amqp://admin:admin@localhost:5672')

CELERY_QUEUE = environ.get('CELERY_QUEUE', 'bullish')

# Django

INSTALLED_APPS += [
    'django_celery_beat',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': environ.get('POSTGRES_DB', 'postgres'),
        'USER': environ.get('POSTGRES_USER', 'postgres'),
        'PASSWORD': environ.get('POSTGRES_PASSWORD', 'postgres'),
        'HOST': environ.get('POSTGRES_HOST', 'localhost'),
        'POST': 5432,
    },
}
