# Generated by Django 3.0.1 on 2019-12-27 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='course',
            field=models.CharField(choices=[('BTECH', 'Btech'), ('MTECH', 'Mtech'), ('BCA', 'BCA'), ('MCA', 'MCA'), ('BSC', 'Bsc'), ('MSC', 'Msc'), ('MBA', 'MBA')], default='CE', max_length=10),
        ),
    ]
