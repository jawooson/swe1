import os
from django.core.wsgi import get_wsgi_application
"""
WSGI config for jwoo_swe1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jwoo_swe1.settings')
application = get_wsgi_application()
