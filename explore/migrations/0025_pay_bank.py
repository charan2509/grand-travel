# Generated by Django 2.2.20 on 2021-05-15 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0024_flight_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='pay',
            name='bank',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
