from django.db import models

'''
作业一
'''


class Worker(models.Model):
    name = models.CharField(max_length=32, verbose_name="工人姓名")
    gender = models.CharField(max_length=2, verbose_name="性别")
    age = models.IntegerField(verbose_name="年龄")
    join_date = models.DateField(verbose_name="入职日期")

    @classmethod
    def get_list(cls, **kwargs):
        filters = {}
        if kwargs.get("id"):
            filters["id"] = kwargs.get('id')
        if kwargs.get("start_date"):
            filters['join_date__lte'] = kwargs.get('start_date')
            return cls.objects.filter(**filters)

    @classmethod
    def create_one(cls, **kwargs):
        return cls.objects.create(
            name=kwargs.get('name'),
            gender=kwargs.get("gender"),
            age=kwargs.get("age"),
            join_date=kwargs.get("join_date"),
        )

    @classmethod
    def delete_all(cls):
        cls.objects.all().delete()

    def modify(self, **kwargs):
        if kwargs.get('name'):
            self.name = kwargs.get('name')
        return self.save()

    @classmethod
    def modify_obj(cls, pk, name):
        worker_obj = cls.objects.get(pk=pk)
        worker_obj.name = name
        return worker_obj.save()


'''
作业二
'''


class Province(models.Model):
    name = models.CharField(max_length=32, verbose_name="省、自治区、直辖市")


class Cities(models.Model):
    name = models.CharField(max_length=128, verbose_name="城市名称")
    province = models.ForeignKey(Province, on_delete=models.CASCADE)


'''
作业三
'''


class Course(models.Model):
    name = models.CharField(max_length=32)


class Student(models.Model):  # 主动维护关系
    name = models.CharField(max_Length=32)
    course = models.ManyToManyField(Course, through="Relation")


class Relation(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    term = models.CharField(max_length=32)
