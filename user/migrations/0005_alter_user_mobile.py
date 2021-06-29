# Generated by Django 3.2.4 on 2021-06-29 12:29

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_user_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=phone_field.models.PhoneField(max_length=10, unique=True),
        ),
    ]
