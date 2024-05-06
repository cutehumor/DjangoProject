# Generated by Django 5.0.3 on 2024-05-04 14:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0004_student_courses'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='enrollment',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='student',
            name='courses',
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='selection.student'),
        ),
    ]
