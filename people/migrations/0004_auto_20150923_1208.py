# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_alter_person_nationality'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='other_nationalities',
            new_name='nationalities',
        ),
        migrations.AlterField(
            model_name='person',
            name='other_names',
            field=models.CharField(help_text=b'Middle names, space separated', max_length=255, blank=True),
        ),
    ]
