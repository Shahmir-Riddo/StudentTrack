# Generated by Django 4.0 on 2023-04-17 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smsapp', '0004_subject_teacher_alter_student_address_result'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='result',
            unique_together={('student', 'subject')},
        ),
    ]