# Generated by Django 5.0.7 on 2024-08-04 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieInfoScreen', '0003_alter_movieset_directorid'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MovieSet',
            new_name='Movie',
        ),
    ]
