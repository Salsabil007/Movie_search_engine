# Generated by Django 5.0.7 on 2024-08-03 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieInfoScreen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieset',
            name='directorID',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
