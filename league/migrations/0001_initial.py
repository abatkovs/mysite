# Generated by Django 2.0.1 on 2018-01-24 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Summoners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summoner_name', models.CharField(max_length=200)),
                ('summoner_id', models.IntegerField(default=0)),
                ('losses', models.IntegerField(default=0)),
                ('wins', models.IntegerField(default=0)),
                ('leagueName', models.CharField(max_length=100)),
                ('rank', models.CharField(max_length=50)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
