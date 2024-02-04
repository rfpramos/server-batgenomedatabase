# Generated by Django 4.2.4 on 2023-10-09 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0002_alter_project_abbr_alter_project_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='source',
            name='accession_no',
        ),
        migrations.RemoveField(
            model_name='source',
            name='type',
        ),
        migrations.RemoveField(
            model_name='source',
            name='type_id',
        ),
        migrations.AddField(
            model_name='isolate',
            name='accession_no',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='isolate',
            name='type',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='isolate',
            name='type_id',
            field=models.IntegerField(blank=True, default=50000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='isolate',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='isolates', to='source.source'),
        ),
    ]