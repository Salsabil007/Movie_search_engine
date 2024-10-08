# Generated by Django 4.1 on 2024-08-02 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_actorproject_featuresproject_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Taggedasproject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieID', models.IntegerField()),
                ('tagID', models.IntegerField()),
                ('tagweight', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tagproject',
            fields=[
                ('tagID', models.IntegerField(primary_key=True, serialize=False)),
                ('tagName', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AddConstraint(
            model_name='taggedasproject',
            constraint=models.UniqueConstraint(fields=('movieID', 'tagID'), name='unique_movieid1_tagid2'),
        ),
        migrations.AlterUniqueTogether(
            name='taggedasproject',
            unique_together={('movieID', 'tagID')},
        ),
    ]
