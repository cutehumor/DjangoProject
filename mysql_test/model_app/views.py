from django.shortcuts import render
from .models import Students
# Create your views here.

def list_students(request):
    students = Students.get_all()
    return render(request, "student.html", locals())

def detail_students(request, pk):
    student = Students.get_one(pk=pk)
    return render(request, "detail.html", locals())

def mod_students(request, pk):
    student = Students.get_one(pk=pk)
    score = request.POST.get('score')
    student.score = score
    student.save()
    return render(request, "detail.html", locals())
