# Generated by Django 4.0 on 2023-04-15 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smsapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='version',
            new_name='grade',
        ),
    ]
