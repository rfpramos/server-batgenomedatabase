# Generated by Django 4.2.4 on 2023-11-25 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0005_remove_source_project_source_project_abbr_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Project',
        ),
    ]
