# Generated by Django 3.2.3 on 2021-05-18 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0038_bus'),
    ]

    operations = [
        migrations.AddField(
            model_name='pay',
            name='mob',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
    ]