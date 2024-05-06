from django.urls import path

from model_app.views import *

urlpatterns = [
    path('list/', list_students),
    path('detail/<pk>/', detail_students),
    path('mod/<pk>/', mod_students),
]
