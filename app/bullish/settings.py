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
    'accounts',
    'shares',
    'django_celery_beat',
]

AUTH_USER_MODEL = 'accounts.User'

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

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': environ.get('PASSWORD_MIN_LENGTH', 8),
        },
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

TEMPLATES += [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'bullish.jinja2.environment'
        },
    },
]

LOGIN_REDIRECT_URL = '/dashboard'
