from django.urls import path
from selection.views import *

urlpatterns = [
    path('register/', register_student, name='register_student'),
    path('login/', login, name='login'),
    path('welcome/<str:student_id>/', welcome, name='welcome'),
    path('select_course/<str:student_id>/', select_course, name='select_course'),
    path('selected_courses/<str:student_id>/', selected_courses, name='selected_courses'),
    path('admin/', admin, name='admin_panel'),
    path('delete_student/<int:student_id>/', delete_student, name='delete_student'),
]
