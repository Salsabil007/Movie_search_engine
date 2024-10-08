# Generated by Django 5.0.7 on 2024-08-04 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieInfoScreen', '0004_rename_movieset_movie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='directorID',
            new_name='directorName',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='AddressSpace1',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='AddressSpace2',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='imdbPictureURL',
        ),
    ]
