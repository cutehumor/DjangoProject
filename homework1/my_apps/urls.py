from django.urls import path, include
from my_apps.views import sun, star, moren

urlpatterns = [
    path('', moren),
    path('sun/', sun),
    path('star/', star),
]
