# Generated by Django 2.0.5 on 2018-06-19 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_modules', '0007_module_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='number_of_users',
        ),
    ]