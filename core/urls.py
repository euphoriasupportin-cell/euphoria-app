from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('download/', views.download_apk, name='download_apk'),
]