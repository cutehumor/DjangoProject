from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField()
    age = models.IntegerField()

    def __str__(self):
        return self.name
