# Generated by Django 5.0.3 on 2024-05-04 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0003_alter_student_student_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(to='selection.course'),
        ),
    ]