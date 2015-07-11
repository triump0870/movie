# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('imdbScore', models.DecimalField(max_digits=2, decimal_places=1)),
                ('popularity', models.DecimalField(max_digits=3, decimal_places=1)),
                ('releaseDate', models.DateField()),
                ('directorName', models.ForeignKey(to='imdb.Director')),
                ('genre', models.ManyToManyField(to='imdb.Genre')),
            ],
        ),
        migrations.AddField(
            model_name='director',
            name='movies',
            field=models.ForeignKey(blank=True, to='imdb.Movie', null=True),
        ),
    ]
