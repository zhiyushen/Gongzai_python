# Generated by Django 2.1.15 on 2023-05-10 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0024_auto_20230510_2121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='openid',
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(default=1, max_length=100, primary_key=True, serialize=False),
        ),
    ]