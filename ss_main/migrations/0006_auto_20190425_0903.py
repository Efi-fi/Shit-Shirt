# Generated by Django 2.2 on 2019-04-25 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ss_main', '0005_auto_20190424_1848'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shirt',
            old_name='describcion',
            new_name='description',
        ),
    ]