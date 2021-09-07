# Generated by Django 3.2.6 on 2021-09-07 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import restapi.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restapi', '0004_alter_received_registry_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dispatched',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registry_number', models.CharField(help_text='File Name. Automatically generated', max_length=8)),
                ('to_whom_sent', models.CharField(help_text='Destination of the document', max_length=255)),
                ('date_of_letter', models.DateField()),
                ('reference_number', models.CharField(help_text='Reference number of the document', max_length=255)),
                ('subject', models.TextField()),
                ('remarks', models.CharField(help_text='Short notes on document', max_length=255)),
                ('file_directory', models.FileField(upload_to='dispatched-files/%y-%m-%d/', validators=[restapi.validators.validate_image_extension])),
                ('date_dispatched', models.DateTimeField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Dispatched',
                'verbose_name_plural': 'Dispatched',
            },
        ),
    ]
