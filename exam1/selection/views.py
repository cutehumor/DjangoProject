from django.shortcuts import render, redirect
from .models import *

def register_student(request):
    """
    注册新学生。

    如果请求方法为POST，则使用提供的姓名和班级名称创建一个新的学生对象，
    生成唯一的学生ID，并重定向到带有学生详情的'registered.html'模板。
    如果请求方法为GET，则渲染'register.html'模板。
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        class_name = request.POST.get('class_name')
        # 创建一个新的学生对象
        student_id = generate_student_id()
        student = Student.objects.create(name=name, class_name=class_name, student_id=student_id)
        return render(request, 'selection/registered.html', {'student_id': student.student_id, 'student_name': student.name})
    else:
        return render(request, 'selection/register.html')

def login(request):
    """
    登录学生。

    如果请求方法为POST，则检查是否提供了学生ID和姓名。
    如果提供了，则将学生ID和姓名存储在会话中，并重定向到'welcome'视图。
    如果没有提供，则使用错误消息渲染'login.html'模板。
    如果请求方法为GET，则渲染'login.html'模板。
    """
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        student_name = request.POST.get('student_name')
        if student_id and student_name:
            request.session['student_id'] = student_id
            request.session['student_name'] = student_name
            return redirect('welcome', student_id=student_id)
        else:
            return render(request, 'selection/login.html', {'error_message': '学生ID和姓名是必填项！'})
    else:
        return render(request, 'selection/login.html')

def welcome(request, student_id):
    """
    欢迎界面。

    使用登录学生的详细信息渲染'welcome.html'模板。
    """
    student = Student.objects.get(student_id=student_id)
    return render(request, 'selection/welcome.html', locals())

def select_course(request, student_id):
    """
    为登录的学生选择课程。

    如果请求方法为POST，则检查学生是否已经选择了课程。
    如果没有选择，则允许学生选择课程，并重定向到'selected_courses'视图。
    如果已选择，则使用错误消息渲染'select_course.html'模板。
    如果请求方法为GET，则渲染'select_course.html'模板。
    """
    student = Student.objects.get(student_id=student_id)
    if request.method == 'POST':
        course_id = request.POST.get('course')
        if not Enrollment.objects.filter(student=student).exists():
            course = Course.objects.get(id=course_id)
            enrollment = Enrollment.objects.create(student=student, course=course)
            enrollment.save()
            return redirect('selected_courses', student_id=student_id)
        else:
            message = "您已经选择了一门课程。"
            return render(request, 'selection/select_course.html', {'student_id': student_id, 'message': message})
    else:
        courses = Course.objects.all()
        if Enrollment.objects.filter(student=student).exists():
            selected_course = Enrollment.objects.get(student=student).course.name
            message = f"您已经选择了课程：{selected_course}。"
            return render(request, 'selection/select_course.html', {'student_id': student_id, 'message': message})
        else:
            return render(request, 'selection/select_course.html', {'student_id': student_id, 'courses': courses})

def selected_courses(request, student_id):
    """
    查看登录学生已选择的课程。

    使用登录学生已选择的课程的详细信息渲染'selected_courses.html'模板。
    """
    student = Student.objects.get(student_id=student_id)
    enrollment = Enrollment.objects.get(student=student)
    course = enrollment.course
    return render(request, 'selection/selected_courses.html', {'student': student, 'course': course})

def generate_student_id():
    """
    生成唯一的学生ID。

    该逻辑假设学生ID是一个简单的递增数字。
    """
    last_student = Student.objects.last()
    if last_student:
        last_id = int(last_student.student_id)
        new_id = last_id + 1
    else:
        new_id = 1
    return str(new_id).zfill(6)  # 将学生ID填充到6位数字

def admin(request):
    """
    管理员面板。

    使用所有学生及其详细信息的列表渲染'admin.html'模板。
    """
    students = Student.objects.all()
    student_data = []
    for student in students:
        student_courses = Enrollment.objects.filter(student=student)
        courses = [enrollment.course.name for enrollment in student_courses]
        student_data.append({
            'name': student.name,
            'class_name': student.class_name,
            'student_id': student.student_id,
            'courses': courses,
        })
    return render(request, 'selection/admin.html', {'students': student_data})

def delete_student(request, student_id):
    """
    删除学生。

    删除提供的学生ID对应的学生，并重定向到管理员面板。
    """
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('admin_panel')
