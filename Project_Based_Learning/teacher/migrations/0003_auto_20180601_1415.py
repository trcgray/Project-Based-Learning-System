# Generated by Django 2.0.5 on 2018-06-01 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_teacher_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='students',
            field=models.ManyToManyField(related_name='teacher', to='student.Student'),
        ),
    ]
