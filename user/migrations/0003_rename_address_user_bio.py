# Generated by Django 3.2.4 on 2021-06-29 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_user_is_superadmin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='address',
            new_name='bio',
        ),
    ]