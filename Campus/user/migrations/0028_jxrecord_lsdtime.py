# Generated by Django 2.1.15 on 2023-05-20 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0027_jxrecord_longruntime'),
    ]

    operations = [
        migrations.AddField(
            model_name='jxrecord',
            name='LSDTime',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]