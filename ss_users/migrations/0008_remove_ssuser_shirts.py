# Generated by Django 2.2 on 2019-04-22 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ss_users', '0007_remove_ssuser_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ssuser',
            name='shirts',
        ),
    ]