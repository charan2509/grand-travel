# Generated by Django 2.2.20 on 2021-05-14 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0016_auto_20210514_2238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pay',
            old_name='name',
            new_name='fname',
        ),
    ]
