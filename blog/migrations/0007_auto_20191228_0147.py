# Generated by Django 3.0.1 on 2019-12-27 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20191228_0145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='pic1',
        ),
        migrations.RemoveField(
            model_name='post',
            name='pic2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='pic3',
        ),
        migrations.RemoveField(
            model_name='post',
            name='pic4',
        ),
        migrations.RemoveField(
            model_name='post',
            name='pic5',
        ),
    ]
