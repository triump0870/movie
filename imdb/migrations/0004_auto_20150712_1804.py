# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0003_remove_director_movies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='directorName',
        ),
        migrations.AddField(
            model_name='movie',
            name='directorName',
            field=models.ManyToManyField(to='imdb.Director'),
        ),
    ]
