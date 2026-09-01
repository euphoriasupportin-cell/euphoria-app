import os
from django.shortcuts import render
from django.http import FileResponse, Http404
from django.conf import settings

def landing_page(request):
    return render(request, 'landing.html')

def download_apk(request):
    # 🔴 এখানে আপনার নতুন ফাইল নাম 'euphoria.apk' দেওয়া হয়েছে
    apk_path = os.path.join(settings.MEDIA_ROOT, 'downloads', 'euphoria.apk')
    
    if os.path.exists(apk_path):
        response = FileResponse(
            open(apk_path, 'rb'), 
            content_type='application/vnd.android.package-archive'
        )
        # ডাউনলোডের সময় ইউজার যে নামে ফাইলটি পাবে
        response['Content-Disposition'] = 'attachment; filename="euphoria.apk"'
        return response
    raise Http404("APK file not found.")