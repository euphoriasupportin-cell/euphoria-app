import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_download.settings')

application = get_wsgi_application()

# 🔴 Vercel-এর জন্য এই লাইনটি আবশ্যক
app = application