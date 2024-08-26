# Generated by Django 4.1 on 2024-08-01 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movieproject',
            fields=[
                ('movieID', models.IntegerField(primary_key=True, serialize=False)),
                ('imdbPictureURL', models.CharField(blank=True, max_length=300, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('genre', models.CharField(blank=True, max_length=200, null=True)),
                ('AddressSpace1', models.CharField(blank=True, max_length=200, null=True)),
                ('AddressSpace2', models.CharField(blank=True, max_length=200, null=True)),
                ('directorID', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
