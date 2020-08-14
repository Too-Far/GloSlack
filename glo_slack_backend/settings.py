"""
Django settings for glo_slack_backend project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import dj_database_url
from pathlib import Path
import os
from dotenv import load_dotenv


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#!+k1i1@@k0cft&(294!p#oin5s1y%lpmujqx)o+w&#c=t*$&#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
# SLACK CREDENTIALS=========================================================
#! Make sure to switch over to .env!!!!!!!!!!!!!!!!
# SLACK_CLIENT_ID = os.getenv.SLACK_CLIENT_ID
# SLACK_CLIENT_SECRET = os.getenv.SLACK_CLIENT_SECRET
# SLACK_VERIFICATION_TOKEN = os.getenv.SLACK_VERIFICATION_TOKEN
# SLACK_SIGNING_SECRET = os.getenv.SLACK_SIGNING_SECRET
# SLACK_BOT_USER_TOKEN = os.getenv.SLACK_BOT_USER_TOKEN
OAUTH_ACCESS_TOKEN = 'xoxp-1304138354420-1321792232528-1314523323505-69e9988e4ef8f5ef559e15a8aaddb6a1'
CLIENT_ID = '1304138354420.1285057341671'
CLIENT_SECRET = 'a0432356f5f6d5736b243b6ded7252a0'
VERIFICATION_TOKEN = 'YgNyfTgccjAXrhkTRAq0kJhz'
SLACK_SIGNING_SECRET = 'ff038b2043d69f7b5da538de2aab2c07'
BOT_USER_ACCESS_TOKEN = 'xoxb-1304138354420-1300012995715-GjMH2UUMrcdPZmDft7v9qnBz'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django',
    'rest_framework',
    'events'
]

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'glo_slack_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'glo_slack_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

prod_db = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)