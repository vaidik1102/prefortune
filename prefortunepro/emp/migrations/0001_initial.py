# Generated by Django 3.0 on 2024-06-04 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=20)),
                ('dept_id', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=20)),
                ('emp_id', models.CharField(max_length=20)),
                ('emp_salary', models.CharField(max_length=20)),
                ('dept_fid', models.CharField(max_length=20)),
            ],
        ),
    ]