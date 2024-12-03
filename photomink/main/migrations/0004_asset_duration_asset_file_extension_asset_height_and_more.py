# Generated by Django 5.1.3 on 2024-11-28 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_asset_processing_error_asset_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='duration',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='file_extension',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='width',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='mime_type',
            field=models.CharField(blank=True, max_length=127, null=True),
        ),
        migrations.AlterField(
            model_name='workspace',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
