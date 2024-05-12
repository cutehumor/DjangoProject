from django.urls import path

from myapp.views import *

app_name = "homework"

urlpatterns = [
    path("list/", list_students, name="list"),
    path("fruit/login/", login_view, name="login"),
    path("fruit/buy/", buy_view, name="buy"),
    path("fruit/cart/", cart_view, name="cart"),
    path("fruit/test/", test_view, name="test"),
]
