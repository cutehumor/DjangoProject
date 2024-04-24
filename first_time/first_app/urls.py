from django.urls import path, include, re_path
from first_app.views import hello, welcome, cars, add, get_msg, get_info, go_hello

urlpatterns = [
    path('hello/', hello),
    re_path(r"welcome/", welcome),
    path("cars/<name>/<power>/", cars),
    re_path(f"re_cars/(?P<name>[a-z]+)/(?P<power>[0-9]+)/", cars),
    path('add/<a>/<b>/', add),
    path('get_msg/<path:msg>/', get_msg),
    path('get_info/<path:msg>/<get_info>/', get_info),
    path('go_hello/', go_hello),
]
