"""
ASGI config for german project.

This module contains the ASGI application used for serving the project.
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'german.settings')

application = get_asgi_application()
