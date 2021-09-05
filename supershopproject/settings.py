import django_heroku

"""
Django settings for supershopproject project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^&riud0z@-47h3yq#iiu$jyv1x0@ny7+&_6kd+gk7o6c-%h=a_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'marketrade.herokuapp.com',
    'localhost',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'shop',
    'whitenoise.runserver_nostatic'
    # 'webpack_loader',
]

MIDDLEWARE_CLASSES = (
    'whitenoise.middleware.WhiteNoiseMiddleware'
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

ROOT_URLCONF = 'supershopproject.urls'

TEMPLATE_DIR = os.path.join(BASE_DIR, 'shop', 'templates', 'shop')
# TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

STATICFILE_DIR = os.path.join(BASE_DIR, 'static')
# STATICFILE_DIR = os.path.join(BASE_DIR, 'client', 'vue-super-shop', 'dist')
# STATICFILE_DIR = os.path.join(BASE_DIR, 'staticfiles')


# STATIC_ROOT = os.path.normpath(os.path.join(BASE_DIR, 'staticfiles'))
# STATIC_ROOT = os.path.normpath(os.path.join(BASE_DIR, 'client', 'vue-super-shop', 'dist'))
# STATIC_ROOT = os.path.normpath(os.path.join(BASE_DIR))
# STATIC_ROOT = 'client/vue-super-shop/dist/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATIC_ROOT = os.path.join(BASE_DIR, 'client', 'vue-super-shop', 'dist')
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'static_root')

STATIC_HOST = 'https://markettrade.herokuapp.com/' if not DEBUG else ''
STATIC_URL = STATIC_HOST + '/static/'
# STATIC_URL = '/static/'
# STATIC_URL = '/client/vue-super-shop/dist/'
# STATIC_URL = '/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [TEMPLATE_DIR, os.path.join('client', 'vue-super-shop', 'dist')],
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ]
        },
    },
]

WSGI_APPLICATION = 'supershopproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    STATICFILE_DIR,
    # os.path.join(BASE_DIR, 'client', 'vue-super-shop', 'dist', 'css'),
    # os.path.join(BASE_DIR, 'client', 'vue-super-shop', 'dist', 'js'),
    # os.path.join(BASE_DIR, 'static', /'static_files'),
    
    # os.path.join(BASE_DIR, "assets"),
    # os.path.join(BASE_DIR, "client/vue-super-shop/dist"),

]

CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = (
    'http://localhost:8080',
)

CORS_ALLOWED_ORIGINS = [
    "https://domain.com",
    "https://api.domain.com",
    "http://localhost:8080",
    "http://127.0.0.1:9000"
]

from corsheaders.defaults import default_methods
CORS_ALLOW_METHODS = list(default_methods) + [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT'
]
from corsheaders.defaults import default_headers

CORS_ALLOW_HEADERS = list(default_headers) + [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'accept-language',
    'x-socket-id',
    'x-access-token',
    'content-language',
]

CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https://\w+\.example\.com$",
]

CORS_URLS_REGEX = r'^.*$'

CORS_ALLOW_CREDENTIALS = True

APPEND_SLASH = False

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR,  'static', 'media')

# WEBPACK_LOADER = {
#     'DEFAULT': {
#         'CACHE': not DEBUG,
#         'BUNDLE_DIR_NAME': 'webpack_bundles/',  # must end with slash
#         'STATS_FILE': BASE_DIR.joinpath('client', 'vue-super-shop', 'webpack-stats.json'),
#         'POLL_INTERVAL': 0.1,
#         'TIMEOUT': None,
#         'IGNORE': [r'.+\.hot-update.js', r'.+\.map']
#     }
# }

# from npm.finders import npm_install
# NPM_ROOT_PATH = os.path.join(BASE_DIR, 'client', 'vue-super-shop')
# npm_install()

# Activate Django-Heroku.
django_heroku.settings(locals())