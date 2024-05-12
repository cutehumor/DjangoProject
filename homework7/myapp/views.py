import hashlib
import time

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from myapp.models import *


# Create your views here.
@cache_page(60)
def list_students(request):
    students = Students.get_all()
    return render(request, "student_list.html", locals())

def login_view(request):
    if request.method == "get":
        return render(request, 'fruits_login.html')
    if request.method == "post":
        name = request.POST.get('name')
        pwd = request.POST.get('pws')
        filters = {
            'name': name,
            'pwd': pwd
        }
        users = Users.get_list(**filters)
        if users:
            user = users.first()
            md5 = hashlib.md5()
            md5.update(name.encode('utf-8'))
            token = md5.hexdigest() + str(time.time())
            user.token = token
            user.save()
            response = HttpResponse('<h3>登录成功</h3>')
            response.set_cookie('user_token', token)
            return response
        else:
            return HttpResponse('<h3>登录失败</h3>')

def buy_view(request):
    return HttpResponse('<h3>立即购买</h3>')

def cart_view(request):
    return HttpResponse('<h3>加入购物车</h3>')

def test_view(request):
    return render(request, 'test_page.html')
