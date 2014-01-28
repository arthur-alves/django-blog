"""
WSGI config for django_blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os, sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
# settings_module = "%s.settings" % PROJECT_ROOT.split(os.sep)[-1]
print PROJECT_ROOT
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_blog.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
