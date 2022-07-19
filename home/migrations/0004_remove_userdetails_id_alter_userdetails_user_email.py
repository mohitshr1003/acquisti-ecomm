# Generated by Django 4.0.6 on 2022-07-19 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_userdetails_second_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='id',
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='user_email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
    ]
