# Generated by Django 2.2.20 on 2021-05-11 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0003_auto_20210511_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactuy',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
