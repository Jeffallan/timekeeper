import os
from os.path import join
from distutils.util import strtobool
import dj_database_url
from configurations import Configuration

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Common(Configuration):

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',


        # Third party apps
        'rest_framework',            # utilities for rest apis
        'rest_framework.authtoken',  # token authentication
        'django_filters',            # for filtering rest endpoints
        'djoser',
        'corsheaders',
        'dry_rest_permissions',
        #'drf_writable_nested',
        'phonenumber_field',

        # Your apps
        'api.apps.users',
        'api.apps.core',
        "api.apps.clients",
        "api.apps.services",
        "api.apps.work",
    )

    # https://docs.djangoproject.com/en/2.0/topics/http/middleware/
    MIDDLEWARE = (
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    ROOT_URLCONF = 'api.urls'
    SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
    WSGI_APPLICATION = 'api.wsgi.application'

    # Email
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

    ADMINS = (
        ('Author', 'info@ravenscurity.net'),
    )

    # Postgres
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get("PG_STRING"),
            conn_max_age=int(os.getenv('POSTGRES_CONN_MAX_AGE', 600))
        )
    }

    # General
    APPEND_SLASH = False
    TIME_ZONE = 'UTC'
    LANGUAGE_CODE = 'en-us'
    # If you set this to False, Django will make some optimizations so as not
    # to load the internationalization machinery.
    USE_I18N = False
    USE_L10N = True
    USE_TZ = True
    LOGIN_REDIRECT_URL = '/'

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.0/howto/static-files/
    STATIC_ROOT = os.path.normpath(join(os.path.dirname(BASE_DIR), 'static'))
    STATICFILES_DIRS = []
    STATIC_URL = '/static/'
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )

    # Media files
    MEDIA_ROOT = join(os.path.dirname(BASE_DIR), 'media')
    MEDIA_URL = '/media/'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': os.path.join(BASE_DIR, 'templates'),
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    # Set DEBUG to False as a default for safety
    # https://docs.djangoproject.com/en/dev/ref/settings/#debug
    DEBUG = strtobool(os.getenv('DJANGO_DEBUG', 'no'))

    # Password Validation
    # https://docs.djangoproject.com/en/2.0/topics/auth/passwords/#module-django.contrib.auth.password_validation
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

    # Logging
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'django.server': {
                '()': 'django.utils.log.ServerFormatter',
                'format': '[%(server_time)s] %(message)s',
            },
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'filters': {
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue',
            },
        },
        'handlers': {
            'django.server': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'django.server',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
            'mail_admins': {
                'level': 'ERROR',
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                'propagate': True,
            },
            'django.server': {
                'handlers': ['django.server'],
                'level': 'INFO',
                'propagate': False,
            },
            'django.request': {
                'handlers': ['mail_admins', 'console'],
                'level': 'ERROR',
                'propagate': False,
            },
            'django.db.backends': {
                'handlers': ['console'],
                'level': 'INFO'
            },
        }
    }

    # Custom user app
    AUTH_USER_MODEL = 'users.User'

    # Django Rest Framework
    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': int(os.getenv('DJANGO_PAGINATION_LIMIT', 500)),
        'DATETIME_FORMAT': '%Y-%m-%dT%H:%M:%S%z',
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer',
        ),
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAuthenticated',
        ],
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.SessionAuthentication',
            'rest_framework.authentication.TokenAuthentication',
            'rest_framework_simplejwt.authentication.JWTAuthentication',
        ),
        'DEFAULT_FILTER_BACKENDS': (
            'django_filters.rest_framework.DjangoFilterBackend',
        ),
    }
    PHONENUMBER_DEFAULT_REGION = 'US'
    # JWT Settings
    SIMPLE_JWT = {'AUTH_HEADER_TYPES': ('JWT',),}

    # djoser
    DJOSER = {
                'USER_ID_FIELD': 'id',
                'LOGIN_FIELD': 'email',
                'SET_PASSWORD_RETYPE': False,
                'LOGOUT_ON_PASSWORD_CHANGE': True,
                'PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND': True,
                'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
                'PASSWORD_RESET_CONFIRM_URL':'#/password-reset-confirm/{uid}/{token}',
                "USERNAME_RESET_CONFIRM_URL": '#/username-reset/{uid}/{token}',
                'ACTIVATION_URL': '#/user-activate/{uid}/{token}',
                'SEND_ACTIVATION_EMAIL': True,
                'SERIALIZERS': {'user_create': 'api.apps.users.serializers.CreateUserSerializer',
                                'user': 'api.apps.users.serializers.UserSerializer',
                                'current_user': 'api.apps.users.serializers.UserSerializer',
                                #'user_delete': 'djoser.serializers.UserDeleteSerializer',
                                },
                'PERMISSIONS': { 'user_delete': ['rest_framework.permissions.IsAdminUser'],
                                 'user_create': ['rest_framework.permissions.IsAdminUser'],
                               },
                'EMAIL': {
                            'activation': 'api.apps.core.email.ActivationEmail',
                            #'confirmation': 'api.apps.core.emails.ConfirmationEmail',
                            'password_reset': 'api.apps.core.email.PasswordResetEmail',
                            #'password_changed_confirmation': 'api.apps.core.emails.PasswordChangedConfirmationEmail',
                            #'username_changed_confirmation': 'api.apps.core.emails.UsernameChangedConfirmationEmail',
                            'username_reset': 'api.apps.core.email.UsernameResetEmail',
                        }
            }

    
    CORS_ORIGIN_WHITELIST = [os.environ.get("CORS_WHITELIST")
                            ]
    ALLOWED_HOSTS = [os.environ.get("ALLOWED_HOSTS")]
    
    CSRF_COOKIE_SAMESITE="Strict"
    SESSION_COOKIE_SAMESITE="Strict"
    #CSRF_TRUSTED_ORIGINS=[] bu default