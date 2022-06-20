# Generated by Django 3.2.13 on 2022-06-20 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('salary_band', models.CharField(max_length=100)),
                ('Q1', models.IntegerField(default=-1)),
                ('Q2', models.IntegerField(default=-1)),
                ('Q3', models.IntegerField(default=-1)),
                ('Q4', models.IntegerField(default=-1)),
                ('Q5', models.IntegerField(default=-1)),
                ('Q6', models.IntegerField(default=-1)),
                ('Q7', models.IntegerField(default=-1)),
                ('Q8', models.IntegerField(default=-1)),
                ('Q9', models.IntegerField(default=-1)),
                ('Q10', models.IntegerField(default=-1)),
            ],
        ),
    ]
