import os
import arrow
from pathlib import Path
from .logger import CustomisedJSONFormatter
from dotenv import load_dotenv

load_dotenv()
BASE_DIR = Path(__file__).resolve().parent

env = os.environ

SECRET_KEY = env.get("SECRET_KEY", "insecure")
DEBUG = env.get("DEBUG", "False") == "True"
ALLOWED_HOSTS = env.get("DJANGO_ALLOWED_HOSTS", "*,").replace('"', "").split(",")

INSTALLED_APPS = [
    # Local apps
    "apps.core",
    "apps.accounts",
    "apps.utils",
    # Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 3rd apps
    "corsheaders",
    "rest_framework",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    "django_elasticsearch_dsl",
    "django_elasticsearch_dsl_drf",
    "minio_storage",
    "django_celery_results",
]

ROOT_URLCONF = "apps.core.urls"
WSGI_APPLICATION = "apps.core.wsgi.application"

AUTH_USER_MODEL = "apps.accounts.models.user.User"

# Database config
DATABASES = {
    "default": {
        "ENGINE": env.get("DATABASE_ENGIN"),
        "NAME": env.get("DATABASE_NAME"),
        "USER": env.get("DATABASE_USER"),
        "PASSWORD": env.get("DATABASE_PASSWORD"),
        "HOST": env.get("DATABASE_HOST"),
        "PORT": env.get("DATABASE_PORT"),
    },
}

# Cache confing
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://redis',
    }
}

# Project middlewares
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Django templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# Authentication backends
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# ELK stack & Logging config
ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'localhost:9200'
    },
}
APP_ID = 'peydayeri'
LOGGING = {
  'version': 1,
  'disable_existing_loggers': False,
  'formatters': {
        'simple': {
            'format': '[%(asctime)s] %(levelname)s|%(name)s|%(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        "json": {
            '()': CustomisedJSONFormatter,
        },
   },
  'handlers': {
        'applogfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': Path(BASE_DIR).resolve().parent.parent.joinpath('logs', 'peydayeri.log'),
            'maxBytes': 1024 * 1024 * 15,  # 15MB
            'backupCount': 10,
            'formatter': 'json',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        }
    },
  'loggers': {
        'django.request': {
            'handlers': ['console', 'applogfile'],
            'level': 'WARNING',
            'propagate': True,
        },
        'core': {
            'handlers': ['console', 'applogfile'],
            'propagate': True,
        },
    }
}

# DRF config
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
    ],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {"anon": "100/day", "user": "1000/day"},
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": env.get("PAGE_SIZE"),
    "DATETIME_FORMAT": "%Y-%m-%d %H:%M:%S%Z",
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.AcceptHeaderVersioning",
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    "TEST_REQUEST_RENDERER_CLASSES": [
        "rest_framework.renderers.MultiPartRenderer",
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.TemplateHTMLRenderer",
    ],
}

# DRF SimpleJWT config
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": arrow.now().shift(hours=5),
    "REFRESH_TOKEN_LIFETIME": arrow.now().shift(days=3),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,

    "ALGORITHM": "HS256",
    "SIGNING_KEY": env.get("SECRET_KEY", "insecure"),
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,

    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",

    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": arrow.now().shift(hours=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": arrow.now().shift(days=3),

    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}

# Files & MinIO config
LOCALE_PATHS = ((Path(BASE_DIR).resolve().parent.parent / "locale"),)

DEFAULT_FILE_STORAGE = "minio_storage.storage.MinioMediaStorage"
STATICFILES_STORAGE = "minio_storage.storage.MinioStaticStorage"
MINIO_STORAGE_ENDPOINT = 'minio:9000'
MINIO_STORAGE_ACCESS_KEY = env.get("MINIO_STORAGE_ACCESS_KEY")
MINIO_STORAGE_SECRET_KEY = env.get("MINIO_STORAGE_SECRET_KEY")
MINIO_STORAGE_USE_HTTPS = False
MINIO_STORAGE_MEDIA_BUCKET_NAME = 'peydayeri-media'
MINIO_STORAGE_AUTO_CREATE_MEDIA_BUCKET = True
MINIO_STORAGE_STATIC_BUCKET_NAME = 'peydayeri-static'
MINIO_STORAGE_AUTO_CREATE_STATIC_BUCKET = True

# Django cors config
CORS_ALLOW_ALL_ORIGINS = env.get("CORS_ALLOW_ALL_ORIGINS", "False") == "True"
CORS_ALLOWED_ORIGIN = env.get("CORS_ALLOWED_ORIGIN", ",").replace('"', "").split(",")

# Localization config
LANGUAGE_CODE = "fa"
TIME_ZONE = "Asia/Tehran"
USE_I18N = True
USE_TZ = True

# Celery config
CELERY_TIMEZONE = "Asia/Tehran"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_BROKER_URL = env.get("CELERY_BROKER")
CELERY_RESULT_BACKEND = env.get("CELERY_BACKEND")
CELERY_CACHE_BACKEND = 'default'

# SMS Panel Configuration
SMS_PHONE_NUMBER = env.get("SMS_PHONE_NUMBER")
SMS_CLIENT_ID = env.get("SMS_CLIENT_ID")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

TEST_RUNNER = "redgreenunittest.django.runner.RedGreenDiscoverRunner"
