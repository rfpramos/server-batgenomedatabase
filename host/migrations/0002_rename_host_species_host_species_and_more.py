# Generated by Django 4.2.4 on 2023-09-18 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='host',
            old_name='host_species',
            new_name='species',
        ),
        migrations.RenameField(
            model_name='host',
            old_name='host_type',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='sample',
            old_name='sample_host',
            new_name='host',
        ),
        migrations.RenameField(
            model_name='sample',
            old_name='sample_type',
            new_name='type',
        ),
    ]