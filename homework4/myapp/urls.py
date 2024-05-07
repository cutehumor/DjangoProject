from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('post-redirect/', views.post_redirect, name='post_redirect'),
    path('result/<str:text>/', views.get_redirect, name='result'),
]
