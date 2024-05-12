from django.db import models

# Create your models here.

# 缓存作业
class Students(models.Model):
    name = models.CharField(max_length=32, verbose_name="姓名")
    score = models.FloatField(verbose_name="成绩")

    class Meta:
        verbose_name = "学生表 (缓存)"
        verbose_name_plural = verbose_name

    @classmethod
    def get_all(cls):
        return cls.objects.all()

# 中间件作业
class Users(models.Model):
    name = models.CharField(max_length=32, verbose_name="用户名")
    pwd = models.CharField(max_length=128, verbose_name="密码")
    token = models.CharField(max_length=256, null=True)

    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    @classmethod
    def get_list(cls, **kwargs):
        filters = {}
        if kwargs.get('name'):
            filters['name'] = kwargs.get('name')
        if kwargs.get('pwd'):
            filters['pwd'] = kwargs.get('pwd')
        if kwargs.get('token'):
            filters['token'] = kwargs.get('token')
        return cls.objects.filter(**filters)
