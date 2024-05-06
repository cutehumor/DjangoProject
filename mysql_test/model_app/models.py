from django.db import models

from model_app.manager import MyManager

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=64)
    history = models.TextField(null=True)

class Students(models.Model):
    name = models.CharField(max_length=32)
    gender = models.CharField(max_length=2)
    score = models.FloatField()
    join_data = models.DateField(null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'students'

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    @classmethod
    def get_one(cls, pk):
        return cls.objects.get(pk=pk)

class Cake(models.Model):
    name = models.CharField(max_length=32)
    price = models.FloatField()
    my_manage = MyManager()

class Person(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.CharField(max_length=2)

class Card(models.Model):
    numbers = models.CharField(max_length=32)
    person = models.OneToOneField(Person, on_delete=models.CASCADE)

class Member(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.CharField(max_length=2)

class Community(models.Model):
    name = models.CharField(max_length=32)
    create_date = models.DateField(null=True)
    members = models.ManyToManyField(Member, through='Relation')

class Relation(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    join_reason = models.CharField(max_length=64, null=True)
