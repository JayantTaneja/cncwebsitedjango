# Generated by Django 3.0.1 on 2019-12-27 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_delete_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pic1',
            field=models.ImageField(default=None, upload_to='static/blog pics'),
        ),
        migrations.AddField(
            model_name='post',
            name='pic2',
            field=models.ImageField(default=None, upload_to='static/blog pics'),
        ),
        migrations.AddField(
            model_name='post',
            name='pic3',
            field=models.ImageField(default=None, upload_to='static/blog pics'),
        ),
        migrations.AddField(
            model_name='post',
            name='pic4',
            field=models.ImageField(default=None, upload_to='static/blog pics'),
        ),
        migrations.AddField(
            model_name='post',
            name='pic5',
            field=models.ImageField(default=None, upload_to='static/blog pics'),
        ),
    ]
