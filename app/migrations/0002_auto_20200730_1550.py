# Generated by Django 2.2 on 2020-07-30 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='Notes',
            new_name='notes',
        ),
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.CharField(max_length=100),
        ),
    ]
