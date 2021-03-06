"""
Django settings for e_commerce project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


ENABLE_SSL = False #Change to true before deploying into production

# if the paypal ipn url == site.name/paypal/endpoint: uses paypal app for the ipn
# else: uses paypal_checkout app for the ipn!!!
# PS: the paypal app is used only to handle the ipn
# but the paypal_checkout app is used to handle everything (ipn if requested, button, return_page, etc)
PAYPAL_TEST = True #Change to false when deploy

PAYPAL_ENVIRONMENT = "sandbox" if PAYPAL_TEST else ""
PAYPAL_HOST = "https://www.sandbox.paypal.com/cgi-bin/webscr/" if PAYPAL_TEST else 'www.paypal.com'
PAYPAL_MERCHANT_ID = 'lucgms-facilitator@gmail.com' if PAYPAL_TEST else os.environ.get('PAYPAL_MERCHANT_ID')
PAYPAL_RECEIVER_EMAIL = 'lucgms-facilitator@gmail.com'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm-$**=gv+y#ux$u)x9f^ic&t=39r6u)y^o)2*$azd=!pegz53d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'myapp',
    'paypal_checkout',
    'paypal.standard.ipn',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # It's commented for now because it's necessary to configure nginx (in pyhton anywhere) to do the 'HTTP_X_FORWARDED_SSL' == 'on'
    # I don't know how to do it yet
    #'SSLMiddleware.SSLRedirect',
)

ROOT_URLCONF = 'e_commerce.urls'

WSGI_APPLICATION = 'e_commerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
