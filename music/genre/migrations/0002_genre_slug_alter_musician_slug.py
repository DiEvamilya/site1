# Generated by Django 4.2.6 on 2023-12-15 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genre', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='musician',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]