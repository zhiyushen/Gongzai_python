# Generated by Django 2.1.15 on 2023-05-10 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0022_auto_20230510_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recodtrain',
            name='user',
        ),
        migrations.DeleteModel(
            name='RecodTrain',
        ),
    ]
