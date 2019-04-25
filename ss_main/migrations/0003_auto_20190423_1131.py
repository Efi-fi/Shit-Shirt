# Generated by Django 2.2 on 2019-04-23 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ss_main', '0002_auto_20190422_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='shirt',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='shirt',
            name='rating',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]
