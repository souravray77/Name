# Generated by Django 3.0.8 on 2020-07-29 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('father_name', models.CharField(max_length=200)),
                ('mother_name', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=100)),
                ('religion', models.CharField(max_length=50)),
                ('user', models.CharField(max_length=500)),
                ('date_of_birth', models.DateField()),
            ],
        ),
    ]