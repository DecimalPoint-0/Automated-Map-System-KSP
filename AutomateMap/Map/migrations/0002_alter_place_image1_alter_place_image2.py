# Generated by Django 4.0.5 on 2022-08-28 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Map', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='image1',
            field=models.FileField(max_length=255, unique=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='place',
            name='image2',
            field=models.FileField(max_length=255, unique=True, upload_to=''),
        ),
    ]
