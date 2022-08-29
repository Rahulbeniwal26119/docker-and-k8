from datetime import datetime
from pathlib import Path
import environ
import os


env = environ.Env()

ROOT_DIR = Path(__file__).resolve(
).parent.parent.parent
APPS_DIR = ROOT_DIR / 'core_apps'


DEBUG = env.bool(
    "DJANGO_DEBUG", default=False)


# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


THIRD_PARTY_APPS = [
    'rest_framework',
    'django_filters',
    'django_countries',
    'phonenumber_field',
    "drf_yasg",
    "corsheaders"
]

LOCAL_APPS = ["core_apps.common",
              "core_apps.profiles", "core_apps.users"]

INSTALLED_APPS = DJANGO_APPS + \
    THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'authors_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(APPS_DIR / 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.auth.context_processors.i18n',  # new
                'django.contrib.auth.context_processors.static',  # new
                'django.contrib.auth.context_processors.tz',  # new
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'authors_api.wsgi.application'

DATABASES = {"default": env.db(
    "DATABASE_URL")}  # new
# new
DATABASES["default"]["ATOMIC_REQUESTS"] = True

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher'
]


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

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SIDE_ID = 1

ADMIN_URL = 'superadmin/'

ADMINS = [("""Rahul Beniwal""",
           "rahulbeniwal26119@gmail.com")]

MANAGERS = ADMINS

STATIC_URL = '/staticfiles/'

STATIC_ROOT = str(
    ROOT_DIR / 'staticfiles')

STATICFILES_DIRS = []

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

MEDIA_URLS = '/mediafiles/'

MEDIA_ROOT = str(
    ROOT_DIR / 'mediafiles')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_URLS_REGEX = r'^/apis/.*$'

if not os.path.exists("logs"):
    os.makedirs("logs")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            # '()': "coloredlogs.ColoredFormatter",
            "format": "%(levelname)s %(name)-12s %(asctime)s"
            " %(module)s %(process)d %(thread)d %(message)s"
        },
        "simple": {
            "format": "{asctime} {levelname} {module} {lineno} {message}",
            "style": "{"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "rich.logging.RichHandler",
            "formatter": "verbose"
        },
        "file": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": f"logs/{datetime.now().date().today()}.logs",
            "maxBytes": 1024 ** 2 * 30,  # 30 MB
            "backupCount": 10000,
            "formatter": 'simple'
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
    "loggers": {
        "author_live": {
            "level": "INFO",
            "handlers": ["console", "file"],
            "propagate": True
        }
    }
}
