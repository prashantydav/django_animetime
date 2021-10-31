# Generated by Django 3.2.7 on 2021-10-31 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnimeList',
            fields=[
                ('anime_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('genre', models.TextField()),
                ('episodes', models.IntegerField(default=12)),
                ('production', models.CharField(max_length=100)),
                ('season', models.TextField(default='2021')),
                ('premeire_date', models.TextField()),
                ('anime_type', models.CharField(default='tv series', max_length=40)),
                ('discription', models.TextField()),
                ('next_episode', models.TextField()),
            ],
        ),
    ]
