"""
Django settings for django_settings project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

"""
# починить отправку данных (Post / )
# настроить django на сервере под 80 порт nginx + gunicorn - PRODUCTION READY
# купить доменное имя .site и подключить сертификат к серверу
# автодокументация -
#
# Перенести admin на навбар
# 0) Писать по pep8(типизация...)
# 1) Спрятать настройки ключи, пароли и тд. в файл .env
# 3) Добавить авторизацию(добавить models tasks)
# 4) Написать свой context processor(Вывод footer и navbar и количество зарегистрированных пользователей
# 6) написать собственный фильтр
# 7) Написать свой simple tag
21) Система рейтинга и комментариев(лайк/дизлайк или баллы)
15) Создать внешнию карточку(include_card.html)
17) Проверить пароль на регулярку(сложность), подтвердите пароль
20) Защита доступа к защищенным старницам другим пользователям
5) Написать собственный middleware
8) Написать свой чат(web sockets)
9) Написать views через класс BaseView(HttpResponse, Json, Html)
10) Написать todo через clear sql
11) Написать cache для данных
12) Добавить docker
13) Celery - задачи в фоне
14) Переписать pagination через class(Создать файл utils.py)
16) Подключить tailwind
18) Добавить скрыть\показать пароль(native js)
19) Обработчик ошибок
21) Логирование
22) Профиль пользователя(аватарка, bio, расширенная модель)
23) Система жалоб и претензий(уведомления(web-sockets/native))
25) TemplateDoesNotExist - во время пересборки
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-p4yrs%2ed=f&=k$es)__pxpow!k^k(vso71elbzn*wfnrevs)s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = ['https://django-server-production-e665.up.railway.app',
                        'https://www.django-server-production-e665.up.railway.app']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_app',
]

MIDDLEWARE = [
    'django_app.middleware.CustomCorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'django_settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'django_app.context_processors.user_count',
                'django_app.context_processors.post_count',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_settings.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    # 'special': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': os.environ["PGDATABASE"],
    #     'USER': os.environ["PGUSER"],
    #     'PASSWORD': os.environ["PGPASSWORD"],
    #     'HOST': os.environ["PGHOST"],
    #     'PORT': os.environ["PGPORT"],
    # }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'django_cache_table',
        'TIMEOUT': '120',
        'OPTIONS': {
            'MAX_ENTIES': 200,
        }
    },
    'ram_cache': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'django_ram_cache_table',
    },
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Etc/GMT-6'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = Path(BASE_DIR / 'static')  # todo ENABLE FOR COLLECT STATIC
STATICFILES_DIRS = [
    # Path(BASE_DIR / 'static'),  # todo DISABLE FOR COLLECT STATIC
    Path(BASE_DIR / 'static_external'),
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
