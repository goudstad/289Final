# Generated by Django 2.2 on 2019-05-26 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hist', '0002_auto_20190525_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decision',
            name='decisionDate',
            field=models.DateField(blank=True),
        ),
    ]
