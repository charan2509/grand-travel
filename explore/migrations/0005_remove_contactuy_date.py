# Generated by Django 2.2.20 on 2021-05-11 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0004_contactuy_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactuy',
            name='date',
        ),
    ]