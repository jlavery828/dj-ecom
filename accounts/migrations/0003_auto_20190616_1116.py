# Generated by Django 2.0.7 on 2019-06-16 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_full_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='active',
            new_name='is_active',
        ),
    ]
