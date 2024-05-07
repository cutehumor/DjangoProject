from django.shortcuts import render, redirect
from django.urls import reverse

def index(request):  # 首页视图函数，显示一个带有输入框的页面
    return render(request, 'index.html')

def post_redirect(request):  # 处理 POST 请求并重定向到结果页面
    if request.method == 'POST':
        # 如果是 POST 请求，获取表单中输入的文本内容
        text = request.POST.get('text')
        # 使用 URL 反向解析重定向到结果页面，并将输入的文本作为参数传递
        return redirect(reverse('myapp:result', kwargs={'text': text}))
    # 如果不是 POST 请求，重定向回首页
    return redirect(reverse('myapp:index'))

def get_redirect(request, text):  # 处理 GET 请求并显示结果页面
    # 接收传递过来的文本内容，显示在结果页面上
    return render(request, 'result.html', {'text': text})
