# Generated by Django 3.1.3 on 2020-11-28 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0002_signup_users_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup_users',
            name='verified_user',
            field=models.BooleanField(default=False),
        ),
    ]
