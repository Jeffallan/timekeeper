import os
from .common import Common
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Local(Common):
    DEBUG = True

    # Testing
    INSTALLED_APPS = Common.INSTALLED_APPS
    INSTALLED_APPS += ('django_nose',)
    TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
    NOSE_ARGS = [
        BASE_DIR,
        '-s',
        '--nologcapture',
        '--with-coverage',
        '--with-progressive',
        '--cover-package=api'
    ]

    # Mail
    EMAIL_HOST = 'mailhog'
    EMAIL_PORT = 1025
    #EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

    CORS_ORIGIN_WHITELIST = [
                            #"http://localhost:3000",
                            #"http://127.0.0.1:3000",
                            "http://frontend:3000",
                            "http://app.local"
                            ]

