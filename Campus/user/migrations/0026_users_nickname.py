# Generated by Django 2.1.15 on 2023-05-10 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0025_auto_20230510_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='nickName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
