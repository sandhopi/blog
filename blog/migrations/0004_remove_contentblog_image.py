# Generated by Django 5.1.7 on 2025-03-21 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_contentblog_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contentblog',
            name='image',
        ),
    ]
