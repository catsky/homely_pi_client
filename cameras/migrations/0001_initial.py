# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('path', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(verbose_name='date created')),
            ],
        ),
    ]
