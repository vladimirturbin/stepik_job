# Generated by Django 3.0.6 on 2020-05-17 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='published_at',
            field=models.DateField(verbose_name='Опубликовано'),
        ),
    ]
