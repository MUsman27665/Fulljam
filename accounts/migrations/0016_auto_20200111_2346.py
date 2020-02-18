# Generated by Django 2.2.4 on 2020-01-11 23:46

import birthday.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_remove_userprofile_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='birthday',
            field=birthday.fields.BirthdayField(default='2000-01-01'),
        ),
    ]
