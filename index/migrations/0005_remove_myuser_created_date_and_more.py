# Generated by Django 4.0.4 on 2022-06-11 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_alter_myuser_publish_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='publish_date',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='updated_date',
        ),
    ]
