# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='macadress',
            name='machine_name',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
