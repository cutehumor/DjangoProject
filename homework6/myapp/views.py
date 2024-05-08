from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Student
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def student_list(request):
    student_list = Student.objects.all()

    # 每页显示 10 条学生信息
    paginator = Paginator(student_list, 10)
    page = request.GET.get('page')

    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # 如果 page 参数不是一个整数，则显示第一页
        students = paginator.page(1)
    except EmptyPage:
        # 如果 page 参数超出范围，则显示最后一页
        students = paginator.page(paginator.num_pages)

    # 计算当前页和总页数
    current_page = students.number
    total_pages = paginator.num_pages

    return render(request, 'student_list.html', locals())
