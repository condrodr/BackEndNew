"""
WSGI config for BackEndNew project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BackEndNew.settings')

application = get_wsgi_application()
"""source .venv/bin/activate"""
"""daphne -b 0.0.0.0 -p 8030 BackEndNew.asgi:application"""