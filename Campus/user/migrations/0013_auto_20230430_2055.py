# Generated by Django 2.1.15 on 2023-04-30 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20230421_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='TainList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.SmallIntegerField(default=1)),
                ('type', models.CharField(blank=True, max_length=20, null=True)),
                ('week', models.SmallIntegerField(default=1)),
                ('trainContent', models.CharField(blank=True, max_length=50, null=True)),
                ('trainName', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'TrainList',
                'managed': True,
            },
        ),
        migrations.DeleteModel(
            name='TrainPlan',
        ),
    ]