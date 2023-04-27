# Generated by Django 4.0 on 2023-04-19 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smsapp', '0006_alter_result_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='smsapp.subject'),
        ),
    ]