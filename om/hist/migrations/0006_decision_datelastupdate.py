# Generated by Django 2.2 on 2019-06-09 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hist', '0005_remove_decision_datelastupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='decision',
            name='DateLastUpdate',
            field=models.DateField(auto_now=True),
        ),
    ]