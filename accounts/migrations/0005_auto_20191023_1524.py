# Generated by Django 2.2.4 on 2019-10-23 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profilephotos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='facebook',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
