# Generated by Django 3.1.3 on 2021-01-08 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='extended',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='signup_users',
        ),
        migrations.AddField(
            model_name='otp_data',
            name='username',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
