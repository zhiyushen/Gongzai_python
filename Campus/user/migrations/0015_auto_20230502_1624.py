# Generated by Django 2.1.15 on 2023-05-02 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_tfrecord'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tfrecord',
            options={'managed': True},
        ),
        migrations.AlterModelTable(
            name='tfrecord',
            table='TFRecord',
        ),
    ]
