# Generated by Django 2.1.15 on 2023-03-25 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20230325_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='chin_level',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='train_abdominalcurl',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='train_chin',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='train_jump',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='train_run',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
