# Generated by Django 2.2.20 on 2021-05-15 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0019_flight_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='price',
        ),
    ]