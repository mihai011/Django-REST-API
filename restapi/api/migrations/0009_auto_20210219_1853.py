# Generated by Django 3.1.7 on 2021-02-19 18:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20210219_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fibonacirequest',
            name='index',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(2)]),
        ),
    ]
