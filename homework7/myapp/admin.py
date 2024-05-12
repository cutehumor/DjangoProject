from django.contrib import admin

from myapp.models import *

# Register your models here.

models = [
    Students,
    Users,
]

admin.site.register(models)
