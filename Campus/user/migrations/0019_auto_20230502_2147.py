# Generated by Django 2.1.15 on 2023-05-02 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_auto_20230502_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jxrecord',
            name='restTime1',
            field=models.SmallIntegerField(blank=True, default=120, null=True),
        ),
        migrations.AlterField(
            model_name='jxrecord',
            name='restTime2',
            field=models.SmallIntegerField(blank=True, default=120, null=True),
        ),
        migrations.AlterField(
            model_name='jxrecord',
            name='restTime3',
            field=models.SmallIntegerField(blank=True, default=120, null=True),
        ),
        migrations.AlterField(
            model_name='jxrecord',
            name='restTime4',
            field=models.SmallIntegerField(blank=True, default=120, null=True),
        ),
        migrations.AlterField(
            model_name='jxrecord',
            name='restTime5',
            field=models.SmallIntegerField(blank=True, default=120, null=True),
        ),
    ]