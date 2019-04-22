# Generated by Django 2.2 on 2019-04-16 16:19

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('auth', '0011_update_proxy_permissions'),
        ('ss_users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MyUser',
            new_name='SSUser',
        ),
        migrations.AlterModelOptions(
            name='ssuser',
            options={'verbose_name': 's/s user', 'verbose_name_plural': 's/s users'},
        ),
    ]