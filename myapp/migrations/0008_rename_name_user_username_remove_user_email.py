# Generated by Django 5.1 on 2024-12-21 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_user_delete_input_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
    ]
