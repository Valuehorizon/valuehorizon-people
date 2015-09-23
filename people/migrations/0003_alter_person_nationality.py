# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_remove_person_full_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='nationality',
            new_name='other_nationalities',
        ),
    ]
