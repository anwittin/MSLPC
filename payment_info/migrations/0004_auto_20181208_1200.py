# Generated by Django 2.1.4 on 2018-12-08 20:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_info', '0003_auto_20181208_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentgoal',
            name='year_goal',
            field=models.PositiveIntegerField(help_text='Use the following format: 20YY', validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(2018)]),
        ),
    ]
