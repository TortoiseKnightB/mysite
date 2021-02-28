"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from .base import *
from pathlib import Path

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(hp3#-vvk^$9=z=twk1x4lx8g31q9%2h*yhm*vubwk)vcr%&a('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysite_db',
        'USER': 'liuyang',
        'PASSWORD': '123456.Ben',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# 发送邮件设置
# https://docs.djangoproject.com/en/3.1/topics/email/
# https://docs.djangoproject.com/en/3.1/ref/settings/#email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'liuyang.knight@qq.com'
EMAIL_HOST_PASSWORD = 'fyowtoucdtckbgfi'  # 授权码
EMAIL_SUBJECT_PREFIX = '[liuyang 的博客]'
EMAIL_USE_TLS = True  # 与 SMTP 服务器通信时，是否启动 TLS 链接（安全链接）
