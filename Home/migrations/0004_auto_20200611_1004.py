# Generated by Django 3.0.6 on 2020-06-11 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_auto_20200610_1815'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sitesetting',
            old_name='servies_notice',
            new_name='services_note',
        ),
    ]
