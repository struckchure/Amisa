# Generated by Django 3.0.6 on 2020-07-03 07:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_auto_20200702_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='passwordreset',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 3, 7, 30, 44, 44)),
        ),
        migrations.AlterField(
            model_name='order',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 3, 10, 25, 44, 44)),
        ),
    ]