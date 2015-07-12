# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0002_movie_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='director',
            name='movies',
        ),
    ]
