# Generated by Django 5.1.3 on 2024-11-27 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ebooks_app', '0002_user_is_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='bio',
        ),
    ]
