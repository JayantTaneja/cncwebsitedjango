# Generated by Django 3.0.1 on 2020-01-01 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20200101_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phoneno',
            field=models.BigIntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='roll_no',
            field=models.BigIntegerField(max_length=99999999999, unique=True),
        ),
    ]
