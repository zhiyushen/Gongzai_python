# Generated by Django 2.1.15 on 2023-05-03 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_auto_20230502_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='jxrecord',
            name='trainDate',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='jxrecord',
            name='trainTime',
            field=models.TimeField(auto_now=True),
        ),
    ]
