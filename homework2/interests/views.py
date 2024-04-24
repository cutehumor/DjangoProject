from django.http import HttpResponse
from django.shortcuts import render
from .models import Interest

# Create your views here.

def collect_interests(request):
    return render(request, 'collect_interests.html')

def show_interests(request):
    interests = request.GET.get('interests', '')
    return render(request, 'show_interests.html', {'interests': interests})

def homework_hobby_page(request):
    return render(request, "hobby_page.html", locals())

def homework_get_data(request):
    hobby = request.GET.get("hobby")
    return render(request, "hobby_info.html", locals())