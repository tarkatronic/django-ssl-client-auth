#!/usr/bin/env python

from distutils.core import setup

setup(name='django-ssl-auth',
      version='0.8.2.3',
      description='Django SSL Client Authentication',
      author='Kimmo Parviainen-Jalanko',
      author_email='kimvais@ssh.com',
      url='https://github.com/kimvais/django-ssl-client-auth/',
      packages=['django_ssl_auth'],
      requires=['Django (>=1.4)']
)
