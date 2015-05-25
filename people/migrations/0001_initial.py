# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gender', models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])),
                ('title', models.CharField(max_length=10, choices=[('DR', 'Dr.'), ('MR', 'Mr.'), ('MS', 'Ms.'), ('MRS', 'Mrs.'), ('SIR', 'Sir'), ('LORD', 'Lord')])),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('other_names', models.CharField(help_text=b'Middle names, comma separated', max_length=255, blank=True)),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('date_of_death', models.DateField(null=True, blank=True)),
                ('profile', models.TextField(help_text=b'Description of Person', blank=True)),
                ('is_deceased', models.BooleanField(default=False)),
                ('full_name', models.CharField(max_length=255, editable=False, blank=True)),
                ('date_modified', models.DateTimeField(auto_now=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('nationality', models.ManyToManyField(related_name='nationalities', null=True, to='countries.Country', blank=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name', 'date_of_birth'],
                'verbose_name': 'Person',
                'verbose_name_plural': 'People',
            },
        ),
    ]
