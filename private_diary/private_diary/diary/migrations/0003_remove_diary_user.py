# Generated by Django 3.1.7 on 2021-04-11 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_auto_20210407_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diary',
            name='user',
        ),
    ]
