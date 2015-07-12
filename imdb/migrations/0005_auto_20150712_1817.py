# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0004_auto_20150712_1804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='directorName',
        ),
        migrations.AddField(
            model_name='movie',
            name='directorName',
            field=models.CharField(default=1, max_length=140),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Director',
        ),
    ]
