#!/usr/bin/env python
import sys

import django
from django.conf import settings
from django.test.runner import DiscoverRunner

settings.configure(
    DEBUG=True,
    DATABASES={'default': {'ENGINE': 'django.db.backends.sqlite3'}},
    ROOT_URLCONF='browser_verification.test_urls',
    INSTALLED_APPS=(
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.staticfiles',
        'browser_verification',
    ),
    MIDDLEWARE_CLASSES=(
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
    ),
    # TEMPLATES = [
    #     {
    #         'BACKEND': 'django.template.backends.django.DjangoTemplates',
    #         'DIRS': [
    #             'browser_verification/test_templates',
    #             'browser_verification/templates/'
    #         ],
    #     }
    # ]
)

django.setup()
failures = DiscoverRunner(verbosity=1, failfast=True)\
        .run_tests(['browser_verification'])
if failures:
    sys.exit(failures)
