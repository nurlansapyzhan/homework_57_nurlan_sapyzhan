# Generated by Django 4.1.7 on 2023-03-01 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hw57', '0002_alter_status_options_alter_task_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Task',
            new_name='Issue',
        ),
    ]
