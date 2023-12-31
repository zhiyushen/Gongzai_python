# Generated by Django 2.1.15 on 2023-04-21 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20230416_2053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='run',
        ),
        migrations.AddField(
            model_name='users',
            name='T1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='T2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='T3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='T4',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='min_score',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='sec_score',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
