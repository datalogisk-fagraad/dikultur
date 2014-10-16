import os
import environ

env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env()

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
get_path = lambda x: os.path.join(BASE_DIR, x)

SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = env('ALLOWED_HOSTS')

AUTH_USER_MODEL = 'core.User'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.facebook',

    'crispy_forms',
    'sekizai',
    'taggit',

    'apps.groups',
    'apps.core',
    'apps.resources',
    'apps.events',
    'apps.blogs',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    'sekizai.context_processors.sekizai',
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

SITE_ID = 1

ROOT_URLCONF = 'dikultur.urls'

WSGI_APPLICATION = 'dikultur.wsgi.application'

DATABASES = {
    'default': env.db(),
}

EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

LANGUAGE_CODE = env('LANGUAGE_CODE')
TIME_ZONE = env('TIME_ZONE')
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_URL = '/media/'
MEDIA_ROOT = get_path('media')
STATIC_URL = '/static/'
STATIC_ROOT = get_path('static')

TEMPLATE_DIRS = (
    get_path('templates'),
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'
ACCOUNT_USER_MODEL_EMAIL_FIELD = 'email'
