import datetime

from django.shortcuts import render

from tem_app.person import Person


# Create your views here.

def tem_var(request, name):
    return render(request, "show_var.html", {'name': name})

def pass_dict(request):
    product = {
        "name": "Django",
        "teacher": "abc",
    }
    return render(request, "show_info.html", {"product": product})

def pass_obj(request):
    person = Person('bcd', 18)
    return render(request, "show_info.html", {"person": person})

def pass_list(request):
    fruits = ["apple", "banana"]
    return render(request, "show_info.html", {"fruits": fruits})

def show_score(request, score):
    return render(request, "tag_if.html", locals())

def show_list(request, ):
    fruits = ["apple", "banana"]
    return render(request, "tag_for.html", locals())

def show_include(request, ):
    return render(request, "tag_include.html", locals())

def show_child(request):
    return render(request, "child.html", locals())

def show_filter(request):
    string = "Hello Django!"
    time = datetime.datetime.now()
    num = 100
    info = '<h3> info的一些信息 </h3>'
    return render(request, "filter.html", locals())
