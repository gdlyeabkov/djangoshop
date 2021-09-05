"""
WSGI config for supershopproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""
from pathlib import Path

import os
import signal

import sys
import traceback

import time

# from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'supershopproject.settings')

# application = get_wsgi_application()
application = DjangoWhiteNoise(application)

# from django.core import management
# management.call_command('flush', verbosity=0, interactive=False)

# execute_from_command_line(["sudo", "apt", "install", "node"])
# execute_from_command_line(["cd", os.path.join(Path(__file__).resolve().parent.parent,  'client', 'vue-super-shop')])
# execute_from_command_line(["npm", "run", "serve"])

# from npm.bindings import npm_run
# from django.core.management import execute_from_command_line
# execute_from_command_line("cd " + os.path.join(Path(__file__).resolve().parent.parent,  'client', 'vue-super-shop'))
# os.chdir(os.path.join(Path(__file__).resolve().parent.parent,  'client', 'vue-super-shop'))
# stderr, stdout = npm_run('serve')

