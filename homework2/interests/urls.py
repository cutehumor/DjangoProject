from django.urls import path
from .views import collect_interests, show_interests, homework_hobby_page, homework_get_data

urlpatterns = [
    # path('', collect_interests, name='collect_interests'),
    # path('show/', show_interests, name='show_interests'),
    path('', homework_hobby_page),
    path('hobby/', homework_get_data),
]
