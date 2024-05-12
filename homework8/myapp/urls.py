from django.urls import path

from .views import *

app_name = 'homework'

urlpatterns = [
    path('upload/', upload_view, name='upload'),
    path('upload/success/<str:file_path>/', show_img, name='success'),
]
