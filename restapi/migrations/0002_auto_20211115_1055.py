# Generated by Django 3.2.6 on 2021-11-15 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispatched',
            name='registry_number',
            field=models.CharField(help_text='File Name.', max_length=8),
        ),
        migrations.AlterField(
            model_name='received',
            name='registry_number',
            field=models.CharField(help_text='File Name.', max_length=8),
        ),
    ]
