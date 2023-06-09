# Generated by Django 4.0 on 2023-04-17 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smsapp', '0003_alter_student_address_alter_student_grade_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, null=True)),
                ('department', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=15, null=True)),
                ('address', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='smsapp.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='smsapp.student')),
            ],
        ),
    ]
