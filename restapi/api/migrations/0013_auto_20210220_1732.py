# Generated by Django 3.1.7 on 2021-02-20 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20210220_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factorialrequest',
            name='response',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='fibonacirequest',
            name='response',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]