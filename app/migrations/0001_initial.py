# Generated by Django 4.1.5 on 2023-02-09 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(max_length=50)),
                ('branch_name', models.CharField(max_length=50)),
                ('semester', models.PositiveIntegerField()),
                ('subject_name', models.CharField(max_length=50)),
                ('qb', models.FileField(upload_to='')),
                ('date', models.DateField()),
            ],
        ),
    ]
