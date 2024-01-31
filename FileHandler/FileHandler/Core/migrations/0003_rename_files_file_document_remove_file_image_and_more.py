# Generated by Django 5.0 on 2024-01-31 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0002_file_files'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='files',
            new_name='document',
        ),
        migrations.RemoveField(
            model_name='file',
            name='image',
        ),
        migrations.RemoveField(
            model_name='file',
            name='name',
        ),
        migrations.RemoveField(
            model_name='file',
            name='time_stamp',
        ),
    ]
