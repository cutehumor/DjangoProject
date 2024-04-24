from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello(request):
    return HttpResponse("<h3 style='color:green'>Hello Django!</h3>")

def welcome(request):
    return HttpResponse("<h3 style='color:green'>Welcome Django!</h3>")

def cars(request, name, power):
    return HttpResponse(f"<h3>mingzi:{name}, mali:{power}</h3>")

def add(request, a, b):

    a = int(a)
    b = int(b)

    return HttpResponse(f"<h3>liang ge shu de he :{a + b}</h3>")

def get_msg(request, msg):
    return HttpResponse(f"<h3>jie shou dao de xiaoxi shi :{msg}</h3>")

def get_info(request, msg, info):
    return HttpResponse(f"<h3>jie shou dao de MSG shi :{msg},jie shou dao de info shi :{info}</h3>")

def go_hello(request):
    return render(request, "hello.html")
