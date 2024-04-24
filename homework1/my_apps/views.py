from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def sun(request):
    return HttpResponse("<h3'>灿烂的太阳</h3>")

def star(request):
    return HttpResponse("<h3'>闪烁的星星</h3>")

def moren(request):
    return HttpResponse("<h3'>弯弯的月亮</h3>")
