# Generated by Django 5.0.3 on 2024-05-04 11:45

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.CharField(default=uuid.uuid4, max_length=36, unique=True),
        ),
    ]
