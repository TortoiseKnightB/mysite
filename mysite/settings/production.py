"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
from .base import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASE_PASSWORD = os.environ['DATABASE_PASSWORD']
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
# EMAIL_PORT = 587
EMAIL_PORT = 465
EMAIL_HOST_USER = 'liuyang.knight@qq.com'
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']  # 授权码
EMAIL_SUBJECT_PREFIX = '[liuyang 的博客]'
# EMAIL_USE_TLS = True  # 与 SMTP 服务器通信时，是否启动 TLS 链接（安全链接）
EMAIL_USE_SSL = True  # 与 SMTP 服务器通信时，是否启动 SSL 链接（安全链接）


ADMINS = (
    ('admin', '	liuyang.knight@qq.com'),
)

# 日志文件
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/home/mysite_debug.log',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}