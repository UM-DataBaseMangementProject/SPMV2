# Generated by Django 3.2 on 2021-04-14 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School_T',
            fields=[
                ('schoolID', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('schoolName', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Department_T',
            fields=[
                ('departmentID', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('departmentName', models.CharField(max_length=30)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spmapp.school_t')),
            ],
        ),
    ]