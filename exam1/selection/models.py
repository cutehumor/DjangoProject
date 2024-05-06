from django.db import models

class Course(models.Model):  # 课程模型。
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):  # 学生模型。学生具有姓名、班级名称和学生ID属性。
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return self.name

class Enrollment(models.Model):  # 选课模型。关联了学生和课程。
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.name} - {self.course.name}"
