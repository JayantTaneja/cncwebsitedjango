# Generated by Django 2.2.10 on 2020-12-28 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20201225_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditions',
            name='browser',
            field=models.CharField(blank=True, default='NA', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='auditions',
            name='ip',
            field=models.CharField(blank=True, default='NA', max_length=1000, null=True),
        ),
    ]
