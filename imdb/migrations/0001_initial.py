# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
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
                ('directorName', models.CharField(max_length=140)),
                ('imdbScore', models.DecimalField(max_digits=2, decimal_places=1)),
                ('popularity', models.DecimalField(max_digits=3, decimal_places=1)),
                ('releaseDate', models.DateField()),
                ('genre', models.ManyToManyField(to='imdb.Genre')),
                ('owner', models.ForeignKey(related_name='movies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
