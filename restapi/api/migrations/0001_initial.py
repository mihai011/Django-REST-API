# Generated by Django 3.1.7 on 2021-02-19 17:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FactorialRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.PositiveBigIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('response', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FibonaciRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.PositiveBigIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('response', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PowerRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base', models.FloatField()),
                ('exponent', models.FloatField()),
                ('response', models.FloatField()),
            ],
        ),
    ]
